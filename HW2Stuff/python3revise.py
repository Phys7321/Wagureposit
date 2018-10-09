# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:09:18 2018
Disc
@author: mattw
"""

import scipy.integrate as scit
import numpy as np
import matplotlib.pyplot as mplot

N = 30
k = 9.0*10**9

v = np.zeros((N,N))

xrange = np.linspace(-3,3,N)
yrange = np.linspace(-3,3,N)
xa,ya = np.meshgrid(xrange,yrange, indexing = 'ij')


for i in range(N):
    for j in range(N):
       xm = xrange[i]
       ym = yrange[j]
 
       fr = lambda xl, yl: k*xl/(np.sqrt((xm-xl)**2+(ym-yl)**2))
       fpol = lambda theta, r: fr(r*np.cos(theta),r*np.sin(theta))*r
       v[i,j],verr = scit.dblquad(fpol, 0, 2, lambda xl: 0, lambda xl: 2*np.pi)
       
ex, ey = np.gradient(-v)

mplot.contour(xa,ya,v,N, cmap="coolwarm")
mplot.quiver(xa,ya,ex,ey)

mplot.show
#graph issue?
