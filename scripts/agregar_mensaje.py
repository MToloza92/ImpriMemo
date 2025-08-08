import json
import os
from pathlib import Path

# Ensure messages directory exists
MESSAGES_DIR = "messages"
Path(MESSAGES_DIR).mkdir(exist_ok=True)

ARCHIVO_MENSAJES = os.path.join(MESSAGES_DIR, "mensajes.json")

def agregar_mensaje(nuevo_mensaje):
    mensajes = []
    if os.path.exists(ARCHIVO_MENSAJES):
        with open(ARCHIVO_MENSAJES, "r", encoding="utf-8") as archivo:
            try:
                mensajes = json.load(archivo)
                if not isinstance(mensajes, list):
                    mensajes = []
            except json.JSONDecodeError:
                mensajes = []

    mensajes.append(nuevo_mensaje)

    with open(ARCHIVO_MENSAJES, "w", encoding="utf-8") as archivo:
        json.dump(mensajes, archivo, indent=2, ensure_ascii=False)

    print(f"Mensaje agregado: '{nuevo_mensaje}'")

if __name__ == "__main__":
    texto = input("Ingresa el mensaje a agregar: ")
    agregar_mensaje(texto)