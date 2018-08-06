#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:06:28 2018

@author: achim
"""
import datetime
import matplotlib.pyplot as plt
import numpy as np

font = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 14,
        }


text_file = open("C://Users//U2683327//Desktop//TempLogger//Daten.dat","r")#/home/achim/Schreibtisch/TempLogger/EEPROMreader/TimeStampData.dat", "r")
data = np.split(np.loadtxt(text_file),3)
#NoOfValues = len(data)


Start = datetime.datetime(2018, 2, 28,  9, 15, 0)
step = datetime.timedelta(minutes=5)
TimeStampArr = []

for i in range(np.size(data)):
    TimeStampArr.append(Start.strftime('%H:%M'))
    Start += step

TimeStamp = np.split(np.array(TimeStampArr),3)    
    
fig, (sb1,sb2,sb3) = plt.subplots(3,1,figsize=(25,10))

x =  np.split( np.arange(0,np.size(data)) ,3)

sb1.plot(x[0],data[0],'r')
sb1.grid()
sb1.set_ylim([0,70])
sb1.set_xticks(x[0])
sb1.set_xticklabels(TimeStamp[0], rotation=90)
sb1.set_ylabel('T in °C', fontdict=font)


sb2.plot(x[1],data[1],'r')
sb2.grid()
sb2.set_ylim([0,70])
sb2.set_xticks(x[1])
sb2.set_xticklabels(TimeStamp[1], rotation=90)
sb2.set_ylabel('T in °C', fontdict=font)

sb3.plot(x[2],data[2],'r')
sb3.grid()
sb3.set_ylim([0,70])
sb3.set_xticks(x[2])
sb3.set_xticklabels(TimeStamp[2], rotation=90)
sb3.set_ylabel('T in °C', fontdict=font)
sb3.set_xlabel('Uhrzeit', fontdict=font)

sb1.set_title('Temperaturverlauf Heizung', fontdict=font)
plt.tight_layout()
plt.savefig("C://Users//U2683327//Desktop//TempLogger//Verlauf.png")

