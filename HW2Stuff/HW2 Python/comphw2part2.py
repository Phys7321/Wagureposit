# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 19:37:10 2018

@author: mattw
"""

import numpy as np
import matplotlib.pyplot as plotlib
import scipy.integrate as scit

rx = input("Lets define a place to determine the potential and E-field ya nerd. What x-coordinate (Numbers not letters)?: ")
ry = input("Okay now asking for a friend but what is the y (Numbers not letters)? ")
# = [2,3] #first define example r then move to other method
rx = float(rx)
ry = float(ry)

k = 9.0 * 10**9

xspace = np.linspace(0,1,20)
yspace = np.linspace(1,2,20)

xpole = lambda x: k*(x**2)/(np.sqrt((rx-x)**2+ry**2))
ypole = lambda y: k*y/(np.sqrt((rx**2)+(ry-y)**2))
 
vx = scit.quad(xpole,0,1)
vy = scit.quad(ypole,1,2)

Ex = np.gradient(vx)
Ey = np.gradient(vy)

Et = Ex + Ey


vtot = vx+vy
vfact = vtot[0]

print("The total potential is: ",vfact)

print("The electric field vector is: ",Et)