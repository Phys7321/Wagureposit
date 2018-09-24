# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 14:56:01 2018

@author: mattw
"""

import numpy as np
import scipy.integrate as scit
import matplotlib.pyplot as maplot

a = 4
x = np.linspace(0,a,20)

ti = lambda x: 4/(np.sqrt(x**4 + a**4))

t = scit.quad(ti, 0, a)
print("Scipy.quad yields: ",t)    

import myint

j= myint.rombergrule(ti,0,a)

print ("myint romer yields: ",j)

i = 0
tm = []
im = []
while i in range(5):
    tq = lambda x: 4/(np.sqrt(x**4 + i**4))
    td = scit.quad(tq, 0, i)
    td0 = float(td[0])
    im.append(i)
    #print (td[0])
    
    i = i + 1
    tm.append(td0)
print (tm)    
print(im)
maplot.plot(im,tm)
maplot.xlabel('Amplitude (a value)')
maplot.ylabel('Period')


