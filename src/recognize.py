import speech_recognition as sr
from gtts import gTTS

import os

# obtain audio from the microphone
def hear():
	while True:
		s = ""
		r = sr.Recognizer()
		with sr.Microphone() as source:
	    		print("Waiting for invoke message - Rachel")
	    		audio = r.listen(source)

		try:
	    		s = r.recognize_google(audio)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
		s = s.lower()
		print("Heard - "+s)
		if s.find("rachel")!=-1 or s.find('richa')!=-1:
			return

def getcommand():
	s = ""
	while True:
		r = sr.Recognizer()
		with sr.Microphone() as source:
	    		print("What Can I Do For You?")
	    		audio = r.listen(source)

		try:
	    		s = r.recognize_google(audio)
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
