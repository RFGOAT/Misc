# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 07:30:59 2017

@author: U2683327
"""

import time

def countdown(t):
    while t > 0:
        print('Remaining: {}s'.format(t))
        time.sleep(1)
        t -= 1
        
while True:
         t = float(input('Countdown time (min):'))
         countdown(t*60)