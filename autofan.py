#!/usr/bin/python

import commands
import time
import sys
#sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib') # Si el sistema es Kodi habilitar esta linea
import RPi.GPIO as GPIO

#GPIO usado para la conexion del ventilador
fan = 17

#Rango de temperatura del CPU
tempA = 37
tempB = 40
tempC = 43
tempD = 46
tempE = 49

GPIO.setmode(GPIO.BCM)
GPIO.setup(fan, GPIO.OUT)
pwm = GPIO.PWM(fan, 1000)

def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000

pwm.start(50)

try:
	while True:
		temp = round(get_cpu_temp())
		if temp <= tempA:
			pwm.ChangeDutyCycle(50)
		elif temp >= tempA+1 and temp <= tempB:
			pwm.ChangeDutyCycle(40)
		elif temp >= tempB+1 and temp <= tempC:
			pwm.ChangeDutyCycle(30)
		elif temp >= tempC+1 and temp <= tempD:
			pwm.ChangeDutyCycle(20)
		elif temp >= tempD+1 and temp <= tempE:
			pwm.ChangeDutyCycle(10)
		elif temp >= tempE+1:
			pwm.ChangeDutyCycle(0)
		time.sleep(1)

except KeyboardInterrupt:
	print ""
	pwm.stop()
	GPIO.cleanup()
