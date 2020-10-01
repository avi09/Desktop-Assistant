import os
import random

import json
import yfinance as yf
import pandas as pd
def open1(s):
	flag = -1
	i = len(s) - 1
	while i>-1 and flag==-1:
		if s[i]==' ' and flag==-1:
			s = s[i+1:]
			flag=1
		else:
			s1 = ''
		i = i - 1
	f = open('open.txt','r')
	x = f.readlines()
	f.close()
	for i in x:
		if i.split('--__')[0] == s:
			os.system(i.split('--__')[1])

def meaning(s):
	flag = -1
	i = len(s) - 1
	while i>-1 and flag==-1:
		if s[i]==' ' and flag==-1:
			s = s[i+1:]
			flag = 1
		else:
			s1=''
		i = i -1
	f = json.load(open('data.json'))
	print('------')
	print(f[s][0])
	print('------')
def string_adjustment(s):
	return s.lower()

def stock(s):
	flag = -1
	i = len(s) - 1
	while i>-1 and flag==-1:
		if s[i]==' ' and flag==-1:
			s = s[i+1:]
			flag=1
		else:
			s1 = ''
		i = i - 1
	d = {'apple':'AAPL', 'google':'GOOG', 'microsoft':'MSFT', 'amazon':'AMZN'}
	s = d[s]
	tick = yf.Ticker(s)
	df = tick.history(period = str(1) + 'd')
	print('------')
	print('Most Recent that I have - \n' + str(df.loc[:,'Close'][0]))
	print('------')
	return
def command(s):
	s = string_adjustment(s)
	if s.find('command')!=-1:
		os.system('python3')
		f = open('1.txt','r')
		x=f.readlines()
		random.shuffle(x)
		return x[1]
	
	elif s.find('meaning')!=-1:
		meaning(s)
		f = open('1.txt','r')
		x = f.readlines()
		random.shuffle(x)
		return x[1]
		
	elif s.find('open')!=-1 or s.find('launch')!=-1:
		open1(s)
		f = open('1.txt','r')
		x=f.readlines()
		random.shuffle(x)
		return x[1]
		
	elif s.find('run')!=-1:
		open1(s)
		f = open('1.txt','r')
		x = f.readlines()
		random.shuffle(x)
		return x[1]
	elif s.find('stock')!=-1 or s.find('share')!=-1:
		stock(s)
		f = open('1.txt','r')
		x = f.readlines()
		random.shuffle(x)
		return x[1]
	else:
		f = open('2.txt','r')
		x=f.readlines()
		random.shuffle(x)
		return x[1]
