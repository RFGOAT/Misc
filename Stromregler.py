# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 07:04:58 2017

@author: U2683327
"""
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(20,690,600)

fig = plt.figure(figsize=(12,7))
I = 0.064/r*1000
plt.plot(r,I)
plt.xticks(np.arange(min(r), max(r)+1, 30.0))
plt.yticks(np.arange(min(I), max(I)+0.2, 0.2))
plt.xlabel('Widerstand Ohm')
plt.ylabel('Strom [mA]')
#plt.show()
plt.grid()

Rges = np.linspace(58,128,20)
Rp = 1/((1/Rges)-(1/680))
print(Rp)
fig2 = plt.figure(figsize=(5,5))
plt.plot(Rp)
plt.show()