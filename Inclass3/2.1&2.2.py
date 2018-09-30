# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:25:23 2018

@author: mattw
"""
import diffeq

T0 = 10.   # initial temperature
Ts = 83.   # temp. of the environment
r = 0.1    # cooling rate
dt = 0.05  # time step
tmax = 60. # maximum time SET TO 10?
nsteps = int(tmax/dt)  # number of steps

T = T0
for i in range(1,nsteps+1):
    new_T = T - r*(T-Ts)*dt
    T = new_T
    #print (i,i*dt, T)
    # we can also do t = t - r*(t-ts)*dt, it would save some memory and processing time.
    
#matplotlib inline
import numpy as np
from matplotlib import pyplot

my_time = np.zeros(nsteps)
my_temp = np.zeros(nsteps)

T = T0
my_temp[0] = T0
for i in range(1,nsteps):
    T = T - r*(T-Ts)*dt
    my_time[i] = i*dt
    my_temp[i] = T
    
pyplot.plot(my_time, my_temp, color='#003366', ls='-', lw=3)
pyplot.xlabel('time')
pyplot.ylabel('temperature');

my_time = np.linspace(0.,tmax,nsteps)

pyplot.plot(my_time, my_temp, color='#003366', ls='-', lw=3)
pyplot.xlabel('time')
pyplot.ylabel('temperature');

def euler(y, f, dx):
    """Computes y_new = y + f*dx
    
    Parameters
    ----------
    y  : float
        old value of y_n at x_n
    f  : float
        first derivative f(x,y) evaluated at (x_n,y_n)
    dx : float
        x step
    """
    
    return y + f*dx

T = T0
for i in range(1,nsteps):
    T = euler(T, -r*(T-Ts), dt)
    my_temp[i] = T
    
euler = lambda y, f, dx: y + f*dx

t10 = []
deltatarr = []

dt = 1.
#my_color = ['#003366','#663300','#660033','#330066']
my_color = ['red', 'green', 'blue', 'black',]


for j in range(0,20): #arbitrarily increase the size
    
    deltatarr.append(dt)
    nsteps = int(tmax/dt)    #the arrays will have different size for different time steps
    my_time = np.linspace(dt,tmax,nsteps) 
    my_temp = np.zeros(nsteps)
    T = T0
    for i in range(1,nsteps):
        T = euler(T, -r*(T-Ts), dt)
        my_temp[i] = T
        if dt*i == 10:
            t10.append(T)
        
    pyplot.plot(my_time, my_temp, ls='-', lw=0.5)
    dt = dt/2.
    
print(t10)
print(deltatarr)
pyplot.xlabel('time');
pyplot.ylabel('temperature');
pyplot.xlim(8,10)
pyplot.ylim(48,58);

fig2 = pyplot.figure(2)
ax2 = fig2.add_subplot(111)
ax2.scatter(deltatarr,t10)

m = diffeq.rk4(-r*(T-Ts))
