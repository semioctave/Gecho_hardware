import RPi.GPIO as GPIO
import subprocess
import time
import AdafruitDHT
from pygame import mixer

mixer.init()
mixer.music.load('./song.mp3')

def led(switch):

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(18,GPIO.OUT)
	print switch
	if switch == "light on":
		GPIO.output(18, GPIO.HIGH)
	elif switch == 'light off' :
		GPIO.output(18,GPIO.LOW)
	elif switch == 'temperature':
		switch = AdafruitDHT.temp()
	elif switch == 'music':
		
		
		if mixer.music.get_busy() == True:
			mixer.music.stop()
			
		else:
			mixer.music.play()
			
	
	
	with open("speech.txt","w") as fp:
		fp.write(switch)

	subprocess.call("espeak -f speech.txt", shell = True)
		
        
