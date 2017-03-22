## AutoFanRaspberry
Con este simple programa coseguiremos refrigerar nuestra Raspberry.

Para empezar, hace una lectura de la temperatura de la CPU.
Según la temperatura variará las revoluciones del ventilador.

### Configuración de Pines
He usado el GPIO18 en BCM y el Pin# 2 de 5v.

![](https://lh4.googleusercontent.com/wH_1kvOPZYzrxHodAodnL5vnziQXTYwIKeDSXmg-gTvh363xsVQxb-nD7NyH3MJwmWcxTnHsvDva6Bo=w1920-h950-rw)

### Instalación

- Instalar Unoffical repository: http://kodi.wiki/view/Unofficial_add-on_repositories
- Buscar e instalar RPi.GPIO
- Copia carpeta **"autofan"** a **"/Storage"**
- Añade la línea **[python /Storage/autofan/autofan.py]** al archivo **"/Configfiles/autostart.sh"**


