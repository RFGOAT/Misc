#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:47:53 2018

@author: achim
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

#Ue = 24
#Ua = 3.3
#Imin = 100
#Imax = 750
#f = 2.5*1000000
#
#rip = np.arange(0.2,0.5,0.1)
#u_rip = 0.1
#
#vt = Ua/Ue
#I = np.linspace(Imin,Imax,50)
#
#
#fig, (ax1, ax2) = plt.subplots(2, 1,figsize=[10,8])
#
#
#for i in rip:
#    Lmin = Ue/(i*I/1000*f)*(vt-vt*vt) * 1000000 #µH
#    ax1.plot(I,Lmin,label='Stromrippel ' + str(int(i*100)) + '%')
#    #Kondensator
##    C_out = (i*I/1000) / (8*u_rip*Ua*f) * 1000000000 #nF -->Thgeorie
##    ax2.plot(I,C_out,label='Stromrippel ' + str(int(i*100)) + '%')
#
#ESR = 10*10**-3
#Cout = np.linspace(1*10**-6, 22*10**-6, 100)
#DV_out = Ua / (f*22*10**-6) * (1-Ua/Ue) * (ESR + 1 / (8*f*Cout))
#ax2.plot(Cout*10**6,DV_out*1000) 
#ax2.set_xlabel('Capacitor [\mF]')   
#ax2.set_ylabel('Spannungsrippel [mV]')
#
#ax1.set_xlabel('Strom [mA]')
##ax2.set_xlabel('Strom [mA]')
#ax1.set_ylabel('Mindestinduktivität [µH]')
##ax2.set_ylabel('Mindestkapazität [nF]')
#
#
#ax1.grid()
#ax2.grid()
#ax1.legend()
#ax2.legend()


fig, (ax1, ax2, ax3) = plt.subplots(3, 1,figsize=[6,8])


ESR = [40*10**-3, 40*10**-3, 40*10**-3]
L = [6*10**-9, 1*10**-9, 0.1*10**-9]
C = [1*10**-6, 100*10**-9, 10*10**-9]

NoOfVal = 100
Zges = np.zeros(NoOfVal) 

f = np.logspace(4, 9, NoOfVal)

for i in range(0,len(ESR)):
    Zi =   np.sqrt( ESR[i]**2 + ( (2*m.pi*f*L[i]) - (1/(2*m.pi*f*C[i])) )**2 )
    ax1.loglog(f,Zi)
    Zges = Zges + (1/Zi)
#    print(Zarr)

ges = 1/Zges

ax1.loglog(f,ges)
ax1.grid()
ax3.loglog(f,ges, label='1000n||100n||1nF')

############
ESR = [40*10**-3, 40*10**-3, 40*10**-3]
L = [6*10**-9, 6*10**-9, 6*10**-9]
C = [1*10**-6, 1*10**-6, 1*10**-6]

NoOfVal = 100
Zges = np.zeros(NoOfVal) 

f = np.logspace(4, 9, NoOfVal)

for i in range(0,len(ESR)):
    Zi =   np.sqrt( ESR[i]**2 + ( (2*m.pi*f*L[i]) - (1/(2*m.pi*f*C[i])) )**2 )
    ax2.loglog(f,Zi)
    Zges = Zges + (1/Zi)
#    print(Zarr)

ges = 1/Zges

ax2.loglog(f,ges)
ax3.loglog(f,ges, label='3x 1000nF')
ax2.grid()
ax3.grid()
ax3.legend()









