# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 12:00:02 2018

@author: mattw
"""

import scipy.integrate as scit
import numpy as np
import matplotlib.pyplot as mplot

N = 30
k = 9.0*10**9
yrange = np.linspace(-2,2,N)
xrange = np.linspace(-2,2,N)
xa,ya = np.meshgrid(xrange,yrange, indexing = 'ij')
Vval = np.zeros((N,N))
#E = np.zeros((N,N))

yrange.reshape(-1 ,1)

x = np.linspace(0,1,50)

for i in range(N):
    for j in range(N):
       xm = xrange[i]
       ym = yrange[j]
       v = lambda x: k*2*x/(np.sqrt((xm-x)**(2)+ym**2))
       Vval[i,j], verr = scit.quad(v,0,1, points=0)

ex, ey = np.gradient(-Vval)

mplot.figure(0)
mplot.contour(xa,ya,Vval,N, cmap = 'coolwarm')
mplot.quiver(xa,ya,ex,ey)


#PART 2

y2range = np.linspace(-1,3,N)
x2range = np.linspace(-1,3,N)
x2a,y2a = np.meshgrid(x2range,y2range, indexing = 'ij')

v2x = np.zeros((N,N))
v2y = np.zeros((N,N))

for l in range(N):
    for k in range(N):
       xm = x2range[l]
       ym = y2range[k]
       v2xf = lambda xl: k*2*xl/(np.sqrt((xm-xl)**(2)+ym**2))
       v2yf = lambda yl: k*yl/(np.sqrt((xm)**(2)+(ym-yl)**2))
       v2y[l,k], vyerr = scit.quad(v2yf,1,2, points=0)
       v2x[l,k], vxerr = scit.quad(v2xf,0,1, points=0)
       
vtot = v2x+v2y

e2x,e2y = np.gradient(-vtot)

mplot.figure(1)
mplot.contour(x2a,y2a,vtot,N,cmap = 'coolwarm')
mplot.quiver(x2a,y2a,e2x,e2y)

