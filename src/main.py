from tkinter import *
import os

import time
import threading
import commands
from recognize import hear, getcommand, say
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


window = Tk()
window.wait_visibility(window)
window.title("Rachel - Voice Assistant")
window.wm_attributes('-alpha',0.8)
entry_text=StringVar()

thread1.start()
def set_size_and_location(window, w, h, x, y):
	w = int(w * window.winfo_screenwidth())
	h = int(h * window.winfo_screenheight())
	x = int(x * window.winfo_screenwidth())
	y = int(y * window.winfo_screenheight())
	window.geometry('%dx%d+%d+%d' % (w,h,x,y))

def hide_and_show_window():
	global window,thread_control,entry
	window.withdraw()
	'''Making The Window Reappear'''
	#hear()
	thread_control=1
	window.update()
	window.deiconify()
	entry.focus_set()


'''Function to Take Input From Text Field And Give In for processing'''
def submit():
	global entry_text,thread_control, head, heading
	thread_control=-1
	'''Getting Query'''
	x = entry_text.get()
	x = x.lower()
	heading.place(relx = 0.20)
	head.set("Processing")
	x1 = commands.command(x, head)
	head.set("Rachel")
	heading.place(relx = 0.45, rely = 0.2)
	hide_and_show_window()

''' Initialization Of GUI,setting size and location'''
set_size_and_location(window,0.25,0.25,0.8,0.1)

'''Set Background Color'''
window.configure(background='black')

'''Adding Heading of Assistant'''
head = StringVar()
head.set("Rachel")
heading = Label( window, textvariable = head, anchor="center", bg='black', fg='white')
heading.place(relx=0.45,rely=0.2)

'''Adding Text Field To Take Commands'''
entry = Entry(window,bd=1,width=int(window.winfo_screenwidth()*0.025), bg='#171c26', textvariable=entry_text)
entry.place(relx=0.1,rely=0.6)
hide_and_show_window()

window.mainloop()
