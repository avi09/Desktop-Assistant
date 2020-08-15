from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

import os
import random
import yfinance as yf
import json

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
	try:
		print(f[s][0])
	except Exception:
		print('Meaning not found')

def string_adjustment(s):
	return s.lower()
	
def stem(s):
  stem = PorterStemmer()
  word_m = WordNetLemmatizer()

  stopwords = ['of','and','can','please','for','hey','be','will','you']
  x = s
  xy=''
  for i in x.split(' '):
    if i in stopwords:
      y=1
    else:
      xy+=i+' '
  x=''
  for i in xy.split(' '):
    y=stem.stem(i)
    x+=y+' '
  return x

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
	try:
		x1 = yf.Ticker(s)
	except Exception:
		print('Stock Not Found')
		flag=-1
	if not flag==-1:
		print('Stock price of '+s+' is - '+str(x1.info['open']))

def command(s):
	s = string_adjustment(s)
	if s.find('command')!=-1:
		os.system(s[8:])
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
	elif s.find('stock')!=-1:
		stock(s)
		f=open('1.txt','r')
		x=f.readlines()
		random.shuffle(x)
		return x[1]
		
	else:
		f = open('2.txt','r')
		x=f.readlines()
		random.shuffle(x)
		return x[1]
