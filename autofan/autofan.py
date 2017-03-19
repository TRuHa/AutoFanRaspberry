#!/usr/bin/python

import sys
sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib')
import RPi.GPIO as GPIO
from time import sleep

Gfan = 18
ciclo = 100
GPIO.setmode(GPIO.BCM)
GPIO.setup(Gfan, GPIO.OUT)
pwm = GPIO.PWM(Gfan, 100)
pwm.start(ciclo)

def get_cpu_temp():
	tempFile = open("/sys/class/thermal/thermal_zone0/temp")
	cpu_temp = tempFile.read()
	tempFile.close()
	return int(cpu_temp)/1000

def get_obj():
	objfile = open("/storage/autofan/obj")
	obj_temp = objfile.read()
	objfile.close()
	return int(obj_temp)

def set_ciclo(ciclo):
	ciclofile = open('/storage/autofan/ciclo', 'w')
	ciclofile.write(str(ciclo))
	ciclofile.close()

try:
	while True:
		temp = get_cpu_temp()
		obj = get_obj()

		if not str(temp) == str(obj):
			if str(temp) > str(obj):
				if not ciclo == 100:
					ciclo = ciclo + 1

			elif str(temp) < str(obj):
				if not ciclo == 20:
					ciclo = ciclo - 1

			pwm.ChangeDutyCycle(ciclo)

			print ciclo
			set_ciclo(ciclo)

		sleep(1)

except KeyboardInterrupt:
	print "\nCancelado por el usuario"

finally:
	pwm.stop()
	GPIO.cleanup()	
	print "\nHasta pronto"
	print ""
