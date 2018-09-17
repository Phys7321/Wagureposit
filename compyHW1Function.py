#Was not certain what the x-values were so used the derdata x values(it also avoided singularities)

xfile = open('derdata.txt','r') #converted to text, saved .spyder-py3
strx = xfile.read().split('\n')
x = [float(dx) for dx in strx]
#x is now an array, apply function to this array
import numpy as np
#import math-sin function doesnt want to work with num arrays
funcy = lambda x: np.sin((1.0/(x*(2.0-x))))**2.0
vfun = np.vectorize(funcy)
fx = vfun(x)
    
import matplotlib.pyplot as pyplt
pyplt.figure(0)
pyplt.plot(x,fx,'b--x')
#

#get central difference
N = len(x)
#First Derivative
df= []
for i in range (0,N):
    h = np.diff(x)
    cdf = (funcy(x[i]+(1/2)*h)-funcy(x[i]+(i-1/2)*h))/h
    df.append(cdf)
pyplt.figure(1)
pyplt.plot(x,df,'r--o')


#2nd derivative
dg=[]
for l in range(0,N):
    g = np.diff(x)
    cdg = (0.5*funcy(x[i]+(1/2)*h)-0.5*funcy(x[i]+(i-1/2)*h))/h
    dg.append(cdg)
pyplt.figure(2)    
pyplt.plot(x,dg,'m--*')

#print (df)
#    return df
