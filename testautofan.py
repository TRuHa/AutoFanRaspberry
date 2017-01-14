#!/usr/bin/python

import commands
import time
import sys
import os
#sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib') # Si el sistema es Kodi habilitar esta linea
import RPi.GPIO as GPIO

#GPIO usado para la conexion del ventilador
Gfan = 17

#Rango de temperatura del CPU
tempA = 37
tempB = 40
tempC = 43
tempD = 46
tempE = 49

GPIO.setmode(GPIO.BCM)
GPIO.setup(Gfan, GPIO.OUT)
pwm = GPIO.PWM(Gfan, 1000)
fan = 50


def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000

pwm.start(50)
os.system('clear')

try:
	while True:
		os.system('clear')
		temp = round(get_cpu_temp())
		print ""
		print "-------------------------------------------------------------"
		print ""
		print "        _____  _   _  _____  _____  ___  _____  _   _        "
		print "       |  _  || | | ||_   _||  _  || __||  _  || \ | |       "
		print "       |  _  || |_| |  | |  | |_| || _| |  _  ||  \| |       "
		print "       |_| |_||_____|  |_|  |_____||_|  |_| |_||_|\__|       "
		print ""
		print "                     === AutoFan 1.0 ===                     "
		print ""
		print "-------------------------------------------------------------"
		print ""
		print "  Este script hace un test de AutoFan.                       "
		print ""
		print "  Con el puede comprobar el correcto funcionamiento,         "
		print "  monitoreo de temperaturas y rendimiento del ventilador.    "
		print ""
		print "-------------------------------------------------------------"
		print "      Temperatura CPU: ", temp, " |  Ventilador al", fan,"%"
		print "-------------------------------------------------------------"
		print ""
		print "Presione [CTRL+C] para abortar."
		time.sleep(1)
		if temp <= tempA:
			pwm.ChangeDutyCycle(50)
			fan = 50
		elif temp >= tempA+1 and temp <= tempB:    
			pwm.ChangeDutyCycle(40)
			fan = 60
		elif temp >= tempB+1 and temp <= tempC:
			pwm.ChangeDutyCycle(30)
			fan = 70
		elif temp >= tempC+1 and temp <= tempD:
			pwm.ChangeDutyCycle(20)
			fan = 80
		elif temp >= tempD+1 and temp <= tempE:
			pwm.ChangeDutyCycle(10)
			fan = 90
		elif temp >= tempE+1:
			pwm.ChangeDutyCycle(0)
			fan = 100

except KeyboardInterrupt:
	print ""
	pwm.stop()
	GPIO.cleanup()
