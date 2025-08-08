import asyncio
from bleak import BleakScanner

async def main():
    print("🔍 Escaneando dispositivos Bluetooth...")
    dispositivos = await BleakScanner.discover()
    for d in dispositivos:
        print(f"Nombre: {d.name} | Dirección: {d.address}")

if __name__ == "__main__":
    asyncio.run(main())

# Nombre: MX06 | Dirección: FF:06:25:13:2E:96