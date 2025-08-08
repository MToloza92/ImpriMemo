import asyncio
from bleak import BleakScanner, BleakClient

async def explorar_dispositivo(nombre_objetivo="MX06"):
    print("Buscando dispositivos...")
    dispositivos = await BleakScanner.discover()

    dispositivo = next((d for d in dispositivos if d.name and nombre_objetivo.lower() in d.name.lower()), None)
    if not dispositivo:
        print("No se encontró el dispositivo.")
        return

    print(f"Conectando a {dispositivo.name}...")
    async with BleakClient(dispositivo) as cliente:
        print("Conectado.")
        print("Servicios y características disponibles:")
        for servicio in cliente.services:
            print(f"Servicio: {servicio.uuid}")
            for char in servicio.characteristics:
                print(f"  └── Característica: {char.uuid} - propiedades: {char.properties}")

asyncio.run(explorar_dispositivo("MX06"))


# Servicios y características disponibles:
# Servicio: 00001800-0000-1000-8000-00805f9b34fb
#   └── Característica: 00002a00-0000-1000-8000-00805f9b34fb - propiedades: ['read', 'write']
# Servicio: 0000ae30-0000-1000-8000-00805f9b34fb
#   └── Característica: 0000ae01-0000-1000-8000-00805f9b34fb - propiedades: ['write-without-response']
#   └── Característica: 0000ae02-0000-1000-8000-00805f9b34fb - propiedades: ['notify']
#   └── Característica: 0000ae03-0000-1000-8000-00805f9b34fb - propiedades: ['write-without-response']
#   └── Característica: 0000ae04-0000-1000-8000-00805f9b34fb - propiedades: ['notify']
#   └── Característica: 0000ae05-0000-1000-8000-00805f9b34fb - propiedades: ['indicate']
#   └── Característica: 0000ae10-0000-1000-8000-00805f9b34fb - propiedades: ['read', 'write']
# Servicio: 0000ae3a-0000-1000-8000-00805f9b34fb
#   └── Característica: 0000ae3b-0000-1000-8000-00805f9b34fb - propiedades: ['write-without-response']
#   └── Característica: 0000ae3c-0000-1000-8000-00805f9b34fb - propiedades: ['notify']