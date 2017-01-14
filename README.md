#AutoFanRaspberry
Con este simple programa coseguiremos refrigerar nuestra Raspberry.

Para empezar hace una lectura de la temperatura de la CPU.
Segun la temperatura variara las revoluciones del ventilador.
#
**Configuracion de Pines**

para este programa he usado el GPio 17 y el PIN 2 de 5v.
#
**Instalacion**

  Raspbian: 
- sudo apt-get install python-dev python-rpi.gpio

  Kodi:
- instalar Unoffical repository, http://kodi.wiki/view/Unofficial_add-on_repositories
- Buscar e instalar RPi.GPIO
- editar autofan.py y testautofan.py y eliminar la # de la linea 6


