# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 06:59:01 2017

@author: U2683327
"""
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(threshold=np.nan)


#
#indices = np.array([10,20,300,4000,50000,600000])
#new = []
#nfills = 5
#
#for i in range(0,np.size(indices)):
#    new = np.append(new,indices[i])
#    for j in range(1,nfills):
#        new = np.append(new,indices[i]+j)
#
#
#for i in range(0,np.size(new)):
#    print(new[i])
#    
    
    


#def ResToTemp(ValueArr, SensorType):
#    
#    if SensorType == 'Pt100':
#        R0 = 100
#    elif SensorType == 'Pt1000':
#        R0 = 1000
#
#    A = 3.9083*10**-3
#    B = -5.775*10**-7
#    
#    ExactTemp = (-A + (A**2 - 4*B*(-ValueArr/R0+1))**0.5 ) / (2*B)
#    
#    return ExactTemp
#
#print(ResToTemp(Analog_In_1_1_Loaded, 'Pt100'))


def FillArrayAfterEveryElement(ArrayToFill,NoOfFills):
    #Does: [10,20,30,40,50]->[10,11,12,20,21,22,30,31,32,40,41,42,50,51,52] for NoOfFills=2
    FilledArray = []
    
    for i in range(0,np.size(ArrayToFill)):
        FilledArray = np.append(FilledArray,ArrayToFill[i])
        for j in range(1,NoOfFills):
            FilledArray = np.append(FilledArray,ArrayToFill[i]+j)
    FilledArray = FilledArray.astype(int)
    return FilledArray


def MovAverage(Arr, FilterDepth):
    cumsum, moving_aves, filled_moving_aves = [0], [], []
    
    for i, x in enumerate(Arr, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=FilterDepth:
            moving_ave = (cumsum[i] - cumsum[i-FilterDepth])/FilterDepth
            moving_aves.append(moving_ave)
    

    filled_moving_aves = np.append(filled_moving_aves,moving_aves[0:FilterDepth-1])
    filled_moving_aves = np.append(filled_moving_aves,moving_aves)
    return filled_moving_aves


#Arr = np.random.random(10)
#FilterDepth = 3
#filt = MovAverage(Arr,FilterDepth)
#print(filt)
#print(np.size(Arr))
#print(np.size(filt))
#print(FilterDepth)


#x = np.arange(0,1000)
#
#
#fig5 = plt.figure(figsize=(18,9))
#
#ax = fig5.add_axes()
#Plot1 = fig5.add_subplot(411)
#
#fig5.canvas.draw()
#
#labels = [item.get_text() for item in ax.get_xticklabels()]
#labels[1] = 'Testing'
#
#ax.set_xticklabels(labels)
#
#
#
#plt.show()


#Arr = [10,11,20,22,30,33,40,50]
#
#def DetectSteps(Arr, Stepsize):
#    out = np.where(np.diff(Arr) > Stepsize)[0] + 1
#                  
#    return out
#
#op = DetectSteps(Arr,3)
#print(Arr)
#print(  op  )






#root = 'Z:\\Mitarbeiter\\Schaefer\\P607_UCS\\Testorder_Schweden\\_ANALYSE\\_Trace_Files\\'
#
#savepath = root + 'Decoded_Sync\\Analog_In_1_5_Entire.dat'
#print(savepath)
#Analog_In_1_5_Entire = np.loadtxt(savepath)*1000
#Analog_In_1_5_Entire = Analog_In_1_5_Entire[400000:600000]     
#
#grad = np.diff(Analog_In_1_5_Entire) 
#grad[grad < 0] = 0
#SlewInd = np.nonzero(grad>1)
#
#
#
#fig, (sb1,sb2) = plt.subplots(2,1,figsize=(18,9))
#
#x = np.linspace(0, np.size(Analog_In_1_5_Entire), np.size(Analog_In_1_5_Entire)) 
#sb1.plot(x,Analog_In_1_5_Entire, label='1_5')
#sb1.vlines(x=SlewInd, ymin=Analog_In_1_5_Entire[SlewInd]-50, ymax=Analog_In_1_5_Entire[SlewInd]+50, color='red', label='chInd')
#sb1.legend(loc='best')
#x = np.linspace(0, np.size(grad), np.size(grad)) 
#sb2.plot(x,grad)
#sb2.plot(x,hilbert(grad))



root = 'Z:\\Mitarbeiter\\Schaefer\\P607_UCS\\BB_192\\Temperaturtest Rastatt\\'

#arr = []
#
#NoOfSamples = 100
#TestRuns = 3
#Steps = 5 #4,8,12,16,20
#
###Building the test array
#arrS = [4,8,12,16,20]
#arrS = np.repeat(arrS,NoOfSamples)
#for i in range(0,TestRuns):
#     arr = np.append(arr,arrS)
#
#
#arr = np.array(arr, dtype=float) #list to array
#exact = [4.1,8.2,12.2,16.1,20.3, 4.1,8.1,12.3,16.2,20.4, 4.2,8.3,12.4,16.5,20.6]
#
#for i in range(0,TestRuns*Steps):
#     for j in range(i*NoOfSamples,(i+1)*NoOfSamples):
#         arr[j] = exact[i]
#
#print(arr)


#NoOfSamples = 100
#TestRuns = 2
#Steps = 5 #4,8,12,16,20
#SampleIndices = np.loadtxt('C:\\_Python\\SampleIndices.txt')
#SampleIndices = SampleIndices.astype(int)
#        
#AdjustedCurr = np.loadtxt(root + 'Decoded\\1stRun\\AdjustedCurr_Entire.dat')
## replacing manually typed values
#Steps = 6 # number 0,4,8,12,16,20
#TestRuns = 2 # Number of Temperatures
#
#AdjustedCurr = np.array(AdjustedCurr[SampleIndices], dtype=float)#list to array
#exactMM_values = [0,4.1,8.2,12.2,16.1,20.3, 0,4.1,8.1,12.3,16.2,20.4]#, 4.2,8.3,12.4,16.5,20.6]
#    
#samplePoints = [1*NoOfSamples,2*NoOfSamples,3*NoOfSamples,4*NoOfSamples, 5*NoOfSamples,
#                7*NoOfSamples,8*NoOfSamples,9*NoOfSamples,10*NoOfSamples,11*NoOfSamples]
#for i in range(0,TestRuns*Steps):
#     for j in samplePoints:#range(i*NoOfSamples,(i+1)*NoOfSamples):
#         AdjustedCurr[j] = exactMM_values[i]





#letters = ['a','b','c','d','e','f','g','h','i','j']
#new_list = []
#n = 3
#for start_index in range(0, len(letters), n):
#    new_list.extend(letters[start_index:start_index+n])
#    new_list.append('x')
#new_list.pop()

#a-b

#a = np.array([1,2,3,4,5])
#b = np.array([8,7,6])
#
#if len(a) < len(b):
#    c = a - b[0:np.size(a)]
#else:
#    c = a[0:np.size(b)] - b
#
#
#print(c)


N = 5
 = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, color='#d62728', yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)



























