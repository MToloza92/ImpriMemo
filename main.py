import asyncio
from app import storage, printer

async def main():
    """
    Flujo principal:
    - Cargar mensajes.
    - Imprimirlos si existen.
    - Borrarlos después de imprimir.
    """
    mensajes = storage.cargar_mensajes()

    if mensajes:
        await printer.imprimir_lista_mensajes(mensajes)
        storage.borrar_mensajes()
        print("Mensajes borrados después de imprimir.")
    else:
        print("No hay mensajes para imprimir.")

if __name__ == "__main__":
    asyncio.run(main())
