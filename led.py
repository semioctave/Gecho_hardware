import RPi.GPIO as GPIO
import subprocess
import time

def led(switch):

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(18,GPIO.OUT)
	print switch
        with open("speech.txt","w") as fp:
            fp.write(switch)

        subprocess.call("espeak -f speech.txt", shell = True)
	if switch == "light on":
		GPIO.output(18, GPIO.HIGH)
	elif switch == 'light off' :
		GPIO.output(18,GPIO.LOW)
        
