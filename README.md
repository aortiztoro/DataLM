# Leap Motion
Instalación del sensor.

1. inicialmente se debe descargar el instalador de Leap Motion versión 2.3.1 en el link https://developer.leapmotion.com/releases. El descargable contiene el ejecutable para instalar el sensor, un README y una carpeta con las librerías y ejemplos necesarias para el funcionamiento.
2. En caso de tener problemas con la ejecución de la instalación debido a los visualizadores del computador, seguir las instrucciones de este link https://forums.leapmotion.com/t/resolved-windows-10-fall-creators-update-bugfix/6585, en donde piden reemplazar los archivos LeapSvc.exe y LeapSvc64.exe que se encuentran adjuntos en este repositorio. Se deben reemplazar en la carpeta C:\Program Files (x86)\Leap Motion\Core Services.
3. Comprobar el funcionamiento del panel de control de Leap Motion

Programa para toma de datos.

1. Crear una carpeta para guardar el codigo CodigoBasisLM.py junto con las librerías Leap.dll, leap.lib, Leap.py, Leap.pyc y LeapPython.pyd. 
2. Conectar el leap y verificar el funcionamiento mediante la app del leap.
3. Crear un entorno virtual con python= 2.7
4. Correr el archivo CodigoBasisLM.py y generar movimientos en el Leap Motion.
