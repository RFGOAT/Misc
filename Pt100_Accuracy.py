# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

#functions
def R_theta_approx(theta,R0):
    val = R0*alpha*theta + R0
    return val
def R_theta_exact(theta,R0):
    val = B*R0*theta*theta + A*R0*theta + R0
    return val

#Temperature
tempRange = np.linspace(0,140,30)
#Constants
R0 = 100
#approx
alpha = 3.85e-3 #1/°C 0...100%
#exact
A = 3.9083e-3
B = -5.775e-7


#plot
fig = plt.figure(figsize=(12,5))

Plot1 = fig.add_subplot(131)
Plot1.set_xlabel(r"$\vartheta$ [°C]", fontdict=font)
Plot1.set_ylabel(r"$R(\vartheta) [\Omega]$", fontdict=font)
Plot1.set_title('Pt100 nach DIN EN 60751', fontdict=font)
Plot1.grid()

#ax = plt.gca()
#ax.ticklabel_format(useOffset=False)

Plot1.plot(tempRange,R_theta_approx(tempRange,R0),'k',label = 'approx')
Plot1.plot(tempRange,R_theta_exact(tempRange,R0),'r',label = 'exact')
legend =plt.legend(loc='upper center')

Plot2 = fig.add_subplot(132)
Approx_error = abs(R_theta_exact(tempRange,R0)-R_theta_approx(tempRange,R0))

Plot2.plot(tempRange,Approx_error)
Plot2.set_xlabel(r"$\vartheta$ [°C]", fontdict=font)
Plot2.set_ylabel(r"$Delta [\Omega]$", fontdict=font)
Plot2.set_title('Approx_Fehler', fontdict=font)
plt.grid()
print(Approx_error)

#genauigkeit mit exakt
print('\n')
print('ClassA_Error')


Plot3 = fig.add_subplot(133)
ClassA_Error = 0.15 + 0.002*tempRange
print(ClassA_Error)

R_theta_plot = R_theta_exact(tempRange,R0)/1
x = np.zeros(tempRange.size)
Plot3.errorbar(tempRange, x, yerr=ClassA_Error)
Plot3.plot(tempRange,ClassA_Error, 'r')
Plot3.plot(tempRange,-ClassA_Error, 'r')
Plot3.set_xlabel(r"$\vartheta$ [°C]", fontdict=font)
Plot3.set_ylabel(r"$ClassA-Error [\Omega]$", fontdict=font)
Plot3.set_title('Genauigkeits_Fehler', fontdict=font)
plt.grid()

fig.tight_layout()
#plt.savefig('C:/Users/U2683327/Desktop/Pt100.jpg')
plt.show()

#
#Calibration
calTemp = 120
print('R_exact von 120°C \t')
print(R_theta_exact(calTemp,R0))
#Gain & Offset
alpha_cal_120 = ((R_theta_exact(calTemp,R0)/R0)-1)/calTemp
print(alpha_cal_120)
R_theta_approx_cal120 = R0*alpha_cal_120*tempRange + R0

#plot
fig2 = plt.figure(figsize=(12,5))
Plot4 = fig2.add_subplot(131)
Plot4.plot(tempRange,R_theta_approx_cal120,'k')
Plot4.plot(tempRange,R_theta_exact(tempRange,R0),'r')
Plot4.set_title('Cal120°C vs quadratic', fontdict=font)
plt.xticks(np.arange(min(tempRange), max(tempRange)+10, 20.0))
plt.grid()

calTemp = 135
print('R_exact von 135°C \t')
print(R_theta_exact(calTemp,R0))
#Gain & Offset
alpha_cal_135 = ((R_theta_exact(calTemp,R0)/R0)-1)/calTemp
print(alpha_cal_135)
R_theta_approx_cal135 = R0*alpha_cal_120*tempRange + R0
Plot5 = fig2.add_subplot(132)
Plot5.plot(tempRange,R_theta_approx_cal135,'k')
Plot5.plot(tempRange,R_theta_exact(tempRange,R0),'r')
Plot5.set_title('Cal135°C vs quadratic', fontdict=font)
plt.xticks(np.arange(min(tempRange), max(tempRange)+10, 20.0))
plt.grid()

Plot6 = fig2.add_subplot(133)
Plot6.plot(tempRange,R_theta_exact(tempRange,R0)-R_theta_approx_cal120,'k')
Plot6.plot(tempRange,R_theta_exact(tempRange,R0)-R_theta_approx_cal135,'r')
Plot6.set_title('Error', fontdict=font)
plt.xticks(np.arange(min(tempRange), max(tempRange)+10, 20.0))
plt.grid()
plt.show()

