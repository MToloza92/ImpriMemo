import json
import os
from pathlib import Path

# Create messages directory if not exists
MESSAGES_DIR = "messages"
Path(MESSAGES_DIR).mkdir(exist_ok=True)

ARCHIVO_MENSAJES = os.path.join(MESSAGES_DIR, "mensajes.json")

def cargar_mensajes():
    if not os.path.exists(ARCHIVO_MENSAJES):
        return []
    
    with open(ARCHIVO_MENSAJES, "r", encoding="utf-8") as archivo:
        try:
            mensajes = json.load(archivo)
            return mensajes if isinstance(mensajes, list) else []
        except json.JSONDecodeError:
            return []

def borrar_mensajes():
    with open(ARCHIVO_MENSAJES, "w", encoding="utf-8") as archivo:
        json.dump([], archivo, indent=2, ensure_ascii=False)