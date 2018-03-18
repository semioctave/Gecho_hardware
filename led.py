import RPi.GPIO as GPIO
import subprocess
import time
import AdafruitDHT
from pygame import mixer
from gtts import gTTS
import os



def led(switch):

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(18,GPIO.OUT)
	print switch
	if switch == "light on":
		mixer.init()
		tts = gTTS(text="Switching on lights", lang='en')
		tts.save("good.mp3")
		mixer.music.load('./good.mp3')
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue
		GPIO.output(18, GPIO.HIGH)
		
	elif switch == 'light off' :
		mixer.init()
		tts = gTTS(text="Switching off lights", lang='en')
		tts.save("good.mp3")
		mixer.music.load('./good.mp3')
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue
		GPIO.output(18,GPIO.LOW)
		
	elif switch == 'temperature':
		switch = AdafruitDHT.temp()
		mixer.init()
		tts = gTTS(text=switch, lang='en')
		tts.save("good.mp3")
		mixer.music.load('./good.mp3')
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue
		
	elif switch == 'music':
		
		if mixer.music.get_busy() == True:
			mixer.music.stop()
		else:
			mixer.init()
			mixer.music.load('./song.mp3')
			mixer.music.play()
	
	else:
		mixer.init()
		tts = gTTS(text="The time is " + switch, lang='en')
		tts.save("good.mp3")
		mixer.music.load('./good.mp3')
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue
			
	
	

		
        
