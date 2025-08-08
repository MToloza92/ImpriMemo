ImpriMemo 🧾🚗
ImpriMemo es una aplicación en Python para imprimir automáticamente mensajes recordatorios en una impresora térmica Bluetooth cuando el celular se conecta al auto.

Características
Detección y conexión a impresora térmica Bluetooth (modelo MX06).

Renderizado de texto a imagen para impresión térmica con manejo de fuentes y ajuste de texto.

Comunicación robusta vía BLE con control de errores usando CRC-8.

Manejo de mensajes guardados localmente en formato JSON.

Impresión secuencial de mensajes pendientes y borrado tras impresión.

Scripts auxiliares para agregar mensajes y escanear dispositivos Bluetooth.

Estructura del proyecto
├── app/
│   ├── bluetooth.py # Módulo principal de conexión BLE e impresión
│   ├── printer.py # Lógica para imprimir listas de mensajes
│   ├── storage.py # Manejo de almacenamiento de mensajes JSON
│   └── init.py
├── assets/
│   └── fonts/ # Fuentes para renderizado de texto
├── messages/
│   └── mensajes.json # Archivo donde se guardan los mensajes pendientes
├── scripts/
│   ├── agregar_mensaje.py # Script para agregar mensajes a imprimir
│   ├── explorar_dispositivo.py # Escanea servicios y características BLE
│   └── scan_bt.py # Escanea dispositivos Bluetooth cercanos
├── main.py # Flujo principal para imprimir mensajes pendientes
├── README.md
└── requirements.txt # Dependencias del proyecto (ej: bleak, Pillow)

Requisitos
Python 3.7 o superior

Librerías:

bleak (Bluetooth Low Energy para Python)

Pillow (Manipulación de imágenes)

Puedes instalar las dependencias con:

pip install -r requirements.txt

Uso
Agregar mensajes para imprimir:

python scripts/agregar_mensaje.py

Escanear dispositivos Bluetooth para verificar impresora:

python scripts/scan_bt.py

Explorar características BLE de la impresora (opcional):

python scripts/explorar_dispositivo.py

Ejecutar la impresión de mensajes pendientes:

python main.py

Cómo funciona
El script principal (main.py) carga los mensajes guardados en messages/mensajes.json.

Se conecta a la impresora MX06 por Bluetooth usando bluetooth.py.

Renderiza el texto en una imagen monocromática adaptada para impresión térmica.

Envía los datos a la impresora con comandos específicos y control CRC.

Borra los mensajes del archivo JSON tras imprimir exitosamente.

Notas
Asegúrate de que la impresora esté encendida y conectada al dispositivo.

Puedes modificar los parámetros de fuente y tamaño en bluetooth.py según tus necesidades.

El proyecto está pensado para impresoras térmicas compatibles BLE con UUIDs estándar.

Licencia
Este proyecto está bajo la licencia MIT.
Puedes usarlo y modificarlo libremente para tus proyectos.

¡Gracias por usar ImpriMemo! 🧾🚗
Si tienes dudas o sugerencias, abre un issue o contáctame.

