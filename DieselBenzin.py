# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 12:59:46 2018

@author: u2683327
"""
import numpy as np
import matplotlib.pyplot as plt

JahresKilometer = np.arange(1000,20000)
AnschDB = [7100,7990]
SteuerDB = [152,30]
VerbrauchDB = [4.5,5.8]

BenzGrPreis = 1.40
PreisLiterDB = [0.89*BenzGrPreis , BenzGrPreis]
Jahre = [5,10]


JahresVerbLiterDB = [JahresKilometer/100*VerbrauchDB[0] , JahresKilometer/100*VerbrauchDB[1] ]
JahresVerbGeldDB  =[JahresVerbLiterDB[0]*PreisLiterDB[0] , JahresVerbLiterDB[1]*PreisLiterDB[1]]




fig, (ax1, ax2) = plt.subplots(2, 1,figsize=[6,8])

GesamtDiesel = AnschDB[0] + Jahre[0] * ( SteuerDB[0] + JahresVerbGeldDB[0] )
GesamtBenzin = AnschDB[1] + Jahre[0] * ( SteuerDB[1] + JahresVerbGeldDB[1] )

ax1.plot(JahresKilometer,GesamtDiesel/1000,label='Diesel')
ax1.plot(JahresKilometer,GesamtBenzin/1000,label='Benzin')
ax1.grid()
ax1.legend()



GesamtDiesel = AnschDB[0] + Jahre[1] * ( SteuerDB[0] + JahresVerbGeldDB[0] )
GesamtBenzin = AnschDB[1] + Jahre[1] * ( SteuerDB[1] + JahresVerbGeldDB[1] )

ax2.plot(JahresKilometer,GesamtDiesel/1000,label='Diesel')
ax2.plot(JahresKilometer,GesamtBenzin/1000,label='Benzin')
ax2.grid()
ax2.legend()
fig.show()

