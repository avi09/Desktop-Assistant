from tkinter import *
import os

import time
import threading
import commands
from recognize import hear, getcommand
'''Thread Control Variable'''
thread_control = -1

'''Threading Function'''
def auto_control():
	global thread_control
	while True:
		'''Hear current audio and use it for processing'''
		if thread_control==1:
			entry_text.set("")
			entry_text.set(getcommand())
			submit()
		else:
			time.sleep(0.4)
	
'''Thread 1'''
thread1 = threading.Thread(target=auto_control)

thread1.start()
def set_size_and_location(window, w, h, x, y):
	w = int(w * window.winfo_screenwidth())
	h = int(h * window.winfo_screenheight())
	x = int(x * window.winfo_screenwidth())
	y = int(y * window.winfo_screenheight())
	window.geometry('%dx%d+%d+%d' % (w,h,x,y))

window = Tk()
entry_text=StringVar()

def hide_and_show_window():
	global window,thread_control,entry
	window.withdraw()
	'''Making The Window Reappear'''
	hear()
	thread_control=1
	window.update()
	window.deiconify()
	entry.focus_set()
		
		
'''Function to Take Input From Text Field And Give In for processing'''
def submit():
	global entry_text,thread_control
	thread_control=-1
	'''Getting Query'''
	x = entry_text.get()	
	x = x.lower()
	x1 = commands.command(x)
	hide_and_show_window()
		
''' Initialization Of GUI,setting size and location'''
set_size_and_location(window,0.15,0.15,0.8,0.1)

'''Set Background Color'''
window.configure(background='#171c26')

'''Adding Heading of Assistant'''
heading = Label( window, text = "Rachel", anchor="center", bg='#171c26', fg='white')
heading.place(relx=0.37,rely=0.2)

'''Adding Text Field To Take Commands'''
entry = Entry(window,bd=1,width=int(window.winfo_screenwidth()*0.015), bg='#171c26', textvariable=entry_text)
entry.place(relx=0.1,rely=0.6)
hide_and_show_window()

window.mainloop()


