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

i = 1
while i <= 10:
	if get_cpu_temp() <= 38:
		pwm.ChangeDutyCycle(50)
		os.system('clear')
		print "Temperatura CPU: ", round(get_cpu_temp())
		print "Ventilador al 50%"
		time.sleep(1)
	elif get_cpu_temp() >= 38 and get_cpu_temp() <= 40:    
		pwm.ChangeDutyCycle(40)
		os.system('clear')
		print "Temperatura CPU: ", round(get_cpu_temp())
		print "Ventilador al 60%"
		time.sleep(1)
	elif get_cpu_temp() >= 41 and get_cpu_temp() <= 43:  
		pwm.ChangeDutyCycle(30)
		os.system('clear')
		print "Temperatura CPU: ", round(get_cpu_temp())
		print "Ventilador al 70%"
		time.sleep(1)
	elif get_cpu_temp() >= 44 and get_cpu_temp() <= 46:
		pwm.ChangeDutyCycle(20)
		os.system('clear')
		print "Temperatura CPU: ", round(get_cpu_temp())
		print "Ventilador al 80%"
		time.sleep(1)
	elif get_cpu_temp() >= 47 and get_cpu_temp() <= 49:
		pwm.ChangeDutyCycle(10)
		os.system('clear')
		print "Temperatura CPU: ", round(get_cpu_temp())
		print "Ventilador al 90%"
		time.sleep(1)
	elif get_cpu_temp() >= 49:
		pwm.ChangeDutyCycle(0)
		os.system('clear')
		print "Temperatura CPU: ", round(get_cpu_temp())
		print "Ventilador al 100%"
		time.sleep(1)
