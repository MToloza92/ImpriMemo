from app.bluetooth import conectar_y_enviar
import asyncio

async def imprimir_lista_mensajes(mensajes):
    """Print a list of messages sequentially"""
    for mensaje in mensajes:
        print(f" Enviando mensaje: {mensaje}")
        try:
            # Add a small delay between messages
            await conectar_y_enviar(mensaje)
            await asyncio.sleep(1)  # Wait between messages
        except Exception as e:
            print(f"Error al imprimir '{mensaje}': {e}")