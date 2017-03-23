## AutoFanRaspberry
Con este simple programa coseguiremos refrigerar nuestra Raspberry.

Para empezar, hace una lectura de la temperatura de la CPU.
Según la temperatura variará las revoluciones del ventilador.

### Configuración de Pines
He usado el GPIO18 en BCM, el Pin# 2 de 5v y un transistor NPN2222.

![autofan](https://raw.githubusercontent.com/TRuHa/AutoFanRaspberry/master/wiki/AutoFan.png)

### Instalación

- Instalar Unoffical repository: http://kodi.wiki/view/Unofficial_add-on_repositories
- Buscar e instalar RPi.GPIO
- Copia carpeta **"autofan"** a **"/Storage"**
- Añade la línea **[python /Storage/autofan/autofan.py]** al archivo **"/Configfiles/autostart.sh"**

### Ejecución

Una vez copiada la carpeta e instalado en el inicio, ejecutamos **objetivo.py** para establecer la temperatura a la que se desea mantener.
También tenemos la opción de ejecutar **monitorCPU.py** para comprobar la temperatura de la CPU, el objetivo y los ciclos del ventilador. De esta forma nos aseguramos el correcto funcionamiento.
