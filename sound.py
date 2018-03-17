#!/usr/bin/python
from led import led
import RPi.GPIO as GPIO
import time
import requests

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def subroutine():
	res = requests.get("http://b4cdb600.ngrok.io/testImage")
	print res.content
	led(res.content)

def callback(channel):
	print "Give a clap to invoke"
	if not GPIO.input(channel):
    
		result = requests.get("http://49db6b58.ngrok.io/invoke")
		print result.content
		time.sleep(5)
		subroutine()
                

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
	time.sleep(1)
