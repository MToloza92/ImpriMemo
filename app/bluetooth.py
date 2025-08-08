import asyncio, struct, logging
from bleak import BleakScanner, BleakClient
from bleak.exc import BleakError
from app.config import printer_name, printer_address, char_uuids
from app.render import render_text_to_image, image_to_printer_data

logger = logging.getLogger("ImpriMemo")

crc_table = [...]  # mismo que antes

def crc8(data):
    crc = 0
    for b in data:
        crc = crc_table[(crc ^ b) & 0xff]
    return crc

def format_command(cmd_id, payload=b""):
    header = bytes([0x51, 0x78, cmd_id, 0x00])
    l = len(payload)
    length_bytes = struct.pack("<H", l)
    pkt = header + length_bytes + payload
    crc = crc8(pkt[2:])
    return pkt + bytes([crc, 0xff])

CMD_INIT = 0xA0
CMD_PRINT = 0xA2
CMD_FEED = 0xA1

async def send_command(client, uuid, cmd_id, payload=b""):
    cmd = format_command(cmd_id, payload)
    for i in range(0, len(cmd), 128):
        await client.write_gatt_char(uuid, cmd[i:i+128], response=False)
        await asyncio.sleep(0.01)

async def find_char(client):
    for uuid in char_uuids:
        try:
            await client.get_characteristic(uuid)
            return uuid
        except:
            continue
    try:
        services = await client.get_services()
        for s in services:
            for c in s.characteristics:
                if "write" in c.properties:
                    try:
                        await client.write_gatt_char(c.uuid, b"\x1B\x40", response=False)
                        return c.uuid
                    except:
                        pass
    except:
        pass
    return None

async def connect_and_print(text):
    try:
        dev = await BleakScanner.find_device_by_address(printer_address, timeout=15)
        if not dev:
            devs = await BleakScanner.discover()
            dev = next((d for d in devs if d.name and printer_name in d.name), None)
        if not dev:
            logger.error("impresora no encontrada")
            return False

        async with BleakClient(dev) as client:
            if not client.is_connected:
                return False
            char = await find_char(client)
            if not char:
                return False
            await send_command(client, char, CMD_INIT, b'\x00\x00\x00')
            await asyncio.sleep(0.2)
            img = render_text_to_image(text)
            data = image_to_printer_data(img)
            if not data:
                return False
            await send_command(client, char, CMD_PRINT, data)
            await asyncio.sleep(0.5)
            await send_command(client, char, CMD_FEED, struct.pack("<H", 10))
            return True
    except Exception as e:
        logger.error(f"error en impresión: {e}")
        return False

def conectar_y_enviar(texto):
    return connect_and_print(texto)