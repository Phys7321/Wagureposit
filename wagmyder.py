# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:50:22 2018

@author: Tom K, Special Guest: Matthew Waguespack
"""

def forwardiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(1,N):
        slop = (f(a+k*h)-f(a+(k-1)*h))/h
        g.append(slop)
    return array(g)
    
def backwardiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N-1):
        slop = (f(a+(k+1)*h)-f(a+k*h))/h
        g.append(slop)
    return array(g)

def centraldiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N):
        slop = (f(a+(k+1/2)*h)-f(a+(k-1/2)*h))/h
        g.append(slop)
    return array(g)

def main(f,a,b,N):
    #my assumptions a,b are indices for the x array, N is the length
    #lets get the 4th and 5th
    from numpy import array
    h=(b-a)/N 
    dfour = []
    dfive = []
    for j in range(0:N):
        derv = ((1/12)*(f(a+(j-2)*h)-(f(a+(j+2)*h)))+(2/3)*((f(a-(j*h))-(f(a+j*h)))))/h
        dfour.append(derv)
    return array(dfour)

    for i in range(0:N):
        dervmore = ((3/640)*(f(a+(j+2.5)*h)-(f(a+(j-2)*h)))+(75/64)*((f(a+(j+0.5)h))-f(a+((j-0.5)*h)))+(25/384)*(f(a+(j-1.5)*h)-(f(a+(j+1.5)*h))))/h
        dfive.append(dervmore)
        
    return array(dfive)
main()