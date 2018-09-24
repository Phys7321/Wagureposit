# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:41:57 2018

@author: mattw
"""
#use sample r= [2,3]

import scipy.integrate as scit
import numpy as np
import matplotlib.pyplot as maplot

   #lets setup an undefined vector r

#def r(x,y):
#    return np.array(x,y)
   
rx = input("Lets define a place to determine the potential and E-field ya nerd. What x-coordinate (Numbers not letters)?: ")
ry = input("Okay now asking for a friend but what is the y (numbers not letters)? ")
# = [2,3] #first define example r then move to other method
rx = float(rx)
ry = float(ry)
x = np.linspace(0,1,20)

k = 9.0*10**9
#WE HAVE SOMETHING LIKE:
#v = lambda xprime: 2*x/(np.sqrt((r[0]-xprime)**2+r[1]**2))
#WE HAVE A CONSTANT y so this will reduce down to one integral
    
    
#x = r[0]
y = 3


v = lambda x: k*2*x/(np.sqrt((rx-x)**(2)+ry**2))

    
vint = scit.quad(v, 0 ,1)
print ("Potential tuple is looking like this guy ---> ",vint)

       #vint is a tuple lets convert this into an array
E = np.gradient(vint)

print ("Yo my dawg your E-field is like ", E)
u,w =(zip(vint))
x0 = u[0]
y0 = w[0] #Error?

#To plot more accurately we will use polar coordinates basing theta on user input
r = np.sqrt(rx**2 + ry**2)
if rx != 0:
    theta = np.arctan(ry/rx) #Will need to correct for theta = 180
if rx == 0 and ry>0:
    theta = np.pi/2 #TIL needs to be in radians
if rx == 0 and ry<0:
    theta = 3*np.pi/2
Etot = np.sqrt(E[0]**2+E[1]**2)
vfig = maplot.figure(0)
axem = vfig.add_subplot(111,projection = 'polar')
Vgraph = axem.scatter(theta, x0, marker = 11)

maplot.xlabel("Theta angle location from inputs")



Egraph = axem.scatter(theta, Etot, marker = '$E$')
maplot.legend([Vgraph,Egraph],['Potential','E-field Magnitude'])
#varray = np.vectorize(v)

# =============================================================================
# Here we now want to see if we can expand over various r we want to make this an iteration
# =============================================================================
i = 0
ys = 0
xs = 0
xpos = []
number = 20
vpos = []
vneg = []
Efield = []

while i < number:
    vplan = lambda x: k*2*x/(np.sqrt((xs-x)**(2)+ys**2))
    vfirst = scit.quad(vplan, 0, 1)
    vpos.append(vfirst[0])
    #want to incorporate a negative side and quarter side next
    vplan2 = lambda x: k*2*x/(np.sqrt((-1*xs-x)**(2)+(-1*ys)**2))
    vfirst2 = scit.quad(vplan2, 0, 1)
    vneg.append(vfirst2[0])
    #end negative
    Ex = np.gradient(vfirst)
    Etots = np.sqrt(Ex[1]**2+Ex[0]**2)
    rs = np.sqrt(xs**2+ys**2)
    xpos.append(rs)
    Efield.append(Etots)
    i = i + 0.5
    ys = ys + 0.5
    xs = xs + 0.5
    

maplot.figure(1)
maplot.scatter(xpos, vpos)
maplot.xlabel("Distance from origin (given as r=sqrt(x^2+y^2)" )
maplot.ylabel("Potential")

maplot.figure(2)
maplot.scatter(xpos,Efield)