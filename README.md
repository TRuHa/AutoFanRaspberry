# AutoFanRaspberry
Con este simple programa coseguiremos refrigerar nuestra Raspberry.

Para empezar hace una lectura de la temperatura de la CPU.
Segun la temperatura variara las revoluciones del ventilador.

### Configuracion de Pines
He usado el GPIO18 en BCM y el Pin# 2 de 5v.

<img_src="https://lh5.googleusercontent.com/lLxLTc5NZzlyPswuJHWHBgHiO4w8pFpwjtut3m7V29E0T1xdw4kmvX9mj0WjUxRrYob3sXyQjsrLDM0=w1422-h923-rw" />

# Instalacion

- instalar Unoffical repository, http://kodi.wiki/view/Unofficial_add-on_repositories
- Buscar e instalar RPi.GPIO
- Copia carpeta **"autofan"** a **"/Storage"**
- Añafe la linea **[python /Storage/autofan/autofan.py]** al archivo **"/Configfiles/autostart.sh"**


