# ImpriMemo 🧾🚗

**ImpriMemo** es una aplicación que imprime automáticamente mensajes recordatorios en una impresora térmica Bluetooth al detectar que el celular se ha conectado al auto.

## Funcionalidades
- Detección automática de conexión Bluetooth.
- Impresión directa de mensajes pendientes.
- Almacenamiento local de mensajes en JSON.
- Control manual y automático de impresión.

## Estructura
- `app/`: Código fuente principal.
- `messages/`: Mensajes pendientes para imprimir.
- `tests/`: Pruebas unitarias.
- `assets/`: Recursos varios (logos, íconos, etc.)

## Requisitos
- Python 3.x
- Biblioteca de Bluetooth (ej: `pybluez`, `bleak`)
- Acceso a impresora térmica compatible

## Cómo usar
```bash
python app/main.py
