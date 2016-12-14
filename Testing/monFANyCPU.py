#!/usr/bin/python

import RPi.GPIO as GPIO
import commands
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 1000)

def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000

pwm.start(50)
os.system('clear')

while True:
	temperatura = round(get_cpu_temp())
	if temperatura <= 38:
		pwm.ChangeDutyCycle(50)
		os.system('clear')
		print "Temperatura CPU: ", temperatura
		print "Ventilador al 50%"
		time.sleep(1)
	elif temperatura >= 38 and temperatura <= 40:    
		pwm.ChangeDutyCycle(40)
		os.system('clear')
		print "Temperatura CPU: ", temperatura
		print "Ventilador al 60%"
		time.sleep(1)
	elif temperatura >= 41 and temperatura <= 43:  
		pwm.ChangeDutyCycle(30)
		os.system('clear')
		print "Temperatura CPU: ", temperatura
		print "Ventilador al 70%"
		time.sleep(1)
	elif temperatura >= 44 and temperatura <= 46:
		pwm.ChangeDutyCycle(20)
		os.system('clear')
		print "Temperatura CPU: ", temperatura
		print "Ventilador al 80%"
		time.sleep(1)
	elif temperatura >= 47 and temperatura <= 49:
		pwm.ChangeDutyCycle(10)
		os.system('clear')
		print "Temperatura CPU: ", temperatura
		print "Ventilador al 90%"
		time.sleep(1)
	elif temperatura >= 49:
		pwm.ChangeDutyCycle(0)
		os.system('clear')
		print "Temperatura CPU: ", temperatura
		print "Ventilador al 100%"
		time.sleep(1)
