🖨️ ImpriMemo

Impresión automática de recordatorios en impresora térmica Bluetooth

📌 Descripción del proyecto

ImpriMemo es una aplicación desarrollada en Python que permite imprimir automáticamente mensajes recordatorios en una impresora térmica Bluetooth (BLE).
El objetivo principal es facilitar la impresión de notas o recordatorios almacenados digitalmente, sin interacción manual, ideal para automatizaciones simples como detección de dispositivos o rutinas diarias.

El sistema gestiona mensajes desde un archivo JSON, los renderiza como imagen y los envía a una impresora térmica Bluetooth compatible.

🎯 Objetivo

Automatizar la impresión de mensajes recordatorios.

Practicar comunicación Bluetooth Low Energy (BLE) en Python.

Aplicar manejo de archivos, renderizado de texto a imagen y control de dispositivos externos.

Implementar un flujo robusto con manejo de errores.

🛠️ Tecnologías utilizadas

Python 3

Bluetooth Low Energy (BLE)

Pillow (PIL) para renderizado de texto a imagen

JSON para almacenamiento de mensajes

CRC-8 para validación de paquetes

Impresora térmica Bluetooth (ej: MX06)

📂 Estructura del proyecto
ImpriMemo/
│
├── app/
│   ├── bluetooth.py        # Conexión BLE y envío de datos a la impresora
│   ├── printer.py          # Lógica de impresión de mensajes
│   └── storage.py          # Gestión de mensajes (cargar, guardar, borrar)
│
├── scripts/
│   ├── agregar_mensaje.py  # Agrega mensajes al archivo JSON
│   ├── scan_bt.py          # Escanea dispositivos Bluetooth cercanos
│   └── explorar_dispositivo.py # Explora servicios y características BLE
│
├── assets/
│   └── fonts/
│       ├── DejaVuSans.ttf
│       └── ARIAL.TTF
│
├── messages/
│   └── mensajes.json       # Mensajes pendientes de impresión
│
├── main.py                 # Flujo principal de la aplicación
└── README.md

🔄 Flujo de funcionamiento

Se detecta o escanea la impresora Bluetooth (BLE).

Se cargan los mensajes desde mensajes.json.

Cada mensaje se renderiza como imagen.

La imagen se divide en paquetes y se envía a la impresora.

Una vez impresos, los mensajes se eliminan del archivo JSON.

🧠 Características principales

✅ Comunicación BLE segmentada por paquetes.

✅ Validación de datos mediante CRC-8.

✅ Renderizado de texto usando fuentes personalizadas.

✅ Manejo de errores ante fallos de conexión o impresión.

✅ Separación clara de responsabilidades por módulo.

▶️ Ejecución del proyecto

Clonar el repositorio:

git clone https://github.com/tu-usuario/imprimemo.git


Ejecutar el flujo principal:

python main.py


Para agregar mensajes:

python scripts/agregar_mensaje.py

📌 Requisitos

Python 3.9 o superior

Impresora térmica Bluetooth compatible

Bluetooth activado en el dispositivo

🚀 Posibles mejoras futuras

Interfaz gráfica (GUI)

Configuración dinámica de impresora

Historial de impresiones

Integración con eventos del sistema (auto, WiFi, horarios)

👨‍💻 Autor

Mauricio Toloza
Estudiante de Análisis y Programación
Proyecto académico y experimental
