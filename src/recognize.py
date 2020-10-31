import speech_recognition as sr
from gtts import gTTS

import os
import threading
import time

heard = False
control = False
r = sr.Recognizer()
audio = ""

def secondary_detect():
	global heard, control, audio, r
	while True:
		s = ""
		if control==True:
			try:
				s = r.recognize_google(audio).lower()
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))
			print('Heard - ' + s)
			if s.find("rachel")!=-1 or s.find("richa")!=-1:
				heard = True
				control = False
				audio = ""
			else:
				heard = False
		else:
			time.sleep(0.4)

secondary_detect_thread = threading.Thread(target = secondary_detect)
secondary_detect_thread.start()

# obtain audio from the microphone
def hear():
	global heard, control, r, audio
	while True:
		s = ""
		with sr.Microphone() as source:
		    print("Waiting for invoke message - Rachel")
		    audio = r.listen(source)
		    control = True
		    if heard==True:
			    control = False
			    heard = False
			    return

def getcommand():
	s = ""
	while True:
		r1 = sr.Recognizer()
		with sr.Microphone() as source:
	    		print("What Can I Do For You?")
	    		audio = r1.listen(source)

		try:
	    		s = r1.recognize_google(audio)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
		s = s.lower()
		print('------')
		print('You Said - '+s)
		print('------')
		return s

def say(s):
	x = 'en'
	myobj = gTTS(text=s, lang=x, slow=False)
	myobj.save("audio.mp3")
	os.system("play audio.mp3")
	return
