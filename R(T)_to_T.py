# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 07:06:07 2018

@author: u2683327
"""
import math

Res0 = 100.0; # Resistance at 0 degC for 400ohm R_Ref
a = .00390830
b = -.000000577500


Res_RTD = float(input('Def R(T)'))

temp_C = -(a*Res0) + math.sqrt(a*a*Res0*Res0 - 4*(b*Res0)*(Res0 - Res_RTD))
temp_C = temp_C / (2*(b*Res0))

print(temp_C)

input()