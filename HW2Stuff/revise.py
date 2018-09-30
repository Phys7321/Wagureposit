# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 12:00:02 2018

@author: mattw
"""

import scipy.integrate as scit
import numpy as np
import matplotlib.pyplot as mplot

N = 50
k = 9.0*10**9

xrange = range(0,N)
yrange = range(0,N)

xa,ya = np.meshgrid(xrange,yrange, indexing = 'ij')
Vval = np.zeros((N,N))
#E = np.zeros((N,N))

x = np.linspace(0,1,50)

for i in xrange:
    for j in yrange:
       v = lambda x: k*2*x/(np.sqrt((i-x)**(2)+j**2))
       vint = scit.quad(v,0,1)
       #print(vint)
       #print(vint[0])
       Vval[i,j] = vint[0]
      # ex , ey = 
       
print(Vval)       
mplot.contour([xa,ya],Vval,N)
 