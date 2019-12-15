#!/usr/bin/python

'''
Spam Sms - Spam your number
This project was created by Dfv47 with Black Coder Crush. 
Copyright 15 - 12 - 2k19 @m_d4fv
'''

try:
        import os,time,sys
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '2':
        exit("[sorry] use python version 3$")

# Color
a='\033[1;30m'
b='\033[1;34m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 

# Banner
def awal():
    print (c+"    ____ "+r+"* "+w+"Author "+r+":"+w+" Dfv47 "+c+"____    ")
    print (c+"   / __/__  ___ ___ _    / __/_ _  ___                     ")
    print (c+"  _\ \/ "+y+"_"+c+" \/ "+y+"_"+c+" `/  ' \  _\ \/  ' \(_-< ")
    print (c+" /___/ .__/\_,_/_/_/_/ /___/_/_/_/___/                     ")
    print (c+"    /_/  "+r+"{ "+a+"Black Coder Crush "+r+"}\n            ")
    
def pilih(): 
    print (c+"  1. "+y+"Spam TRI")
    pilih=int(input(b+'\n  ┌─['+a+'spam'+r+'@'+a+'sms'+b+']\n'+b+'  └─['+c+'$'+b+'] '))
    if pilih == 1:
       import data.tri

def start():
    os.system('clear')
    awal() 
    pilih()
    
if __name__=='__main__':
    start()
