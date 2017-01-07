#!/usr/bin/python

<<<<<<< HEAD
import sys
=======
distro = open("/etc/issue","r")
if distro.read() < "OpenELEC":
	import sys
	sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib')
distro.close()

import RPi.GPIO as GPIO
>>>>>>> origin/master
import commands
import time
#sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib') # Si el sistema es Kodi habilitar esta linea
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 1000)

def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000

pwm.start(50)

try:
	while True:
		temp = round(get_cpu_temp())
		if temp <= 38:
			pwm.ChangeDutyCycle(50)
		elif temp >= 38 and temp <= 40:
			pwm.ChangeDutyCycle(40)
		elif temp >= 41 and temp <= 43:
			pwm.ChangeDutyCycle(30)
		elif temp >= 44 and temp <= 46:
			pwm.ChangeDutyCycle(20)
		elif temp >= 47 and temp <= 49:
			pwm.ChangeDutyCycle(10)
		elif temp >= 49:
			pwm.ChangeDutyCycle(0)
		time.sleep(30)

except KeyboardInterrupt:
	print ""
	pwm.stop()
	GPIO.cleanup()
