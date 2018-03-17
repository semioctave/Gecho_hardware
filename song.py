from pygame import mixer

def song(flag)
	
	if flag == 1:
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue
	else
