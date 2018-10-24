import numpy as np
x = np.linspace(1,10)

#vfun = np.vectorize(funcy,otypes = [np.float])
fx = []
for i in x:
    funcy = np.sin((1.0/(i*(2.0-i))))**2.0
    fx.append(funcy)
    
import matplotlib.pyplot as pyplt
pyplt.figure(0)
pyplt.plot(x,fx,'b--x')
pyplt.title('fx vs x')
#

#get central difference
N = len(x)
#First Derivative
df= []
funcy = lambda x: np.sin((1.0/(x*(2.0-x))))**2.0
for i in range (0,N):
    h = np.diff(x)
    cdf = (funcy(x[i]+(1/2)*h)-funcy(x[i]+(i-1/2)*h))/h
    df.append(cdf)
pyplt.figure(1)
pyplt.plot(x,df,'r--o')
pyplt.title("First Derivative")


#2nd derivative
dg=[]
for l in range(0,N):
    g = np.diff(x)
    cdg = (0.5*funcy(x[i]+(1/2)*h)-0.5*funcy(x[i]+(i-1/2)*h))/h
    dg.append(cdg)
pyplt.figure(2)    
pyplt.plot(x,dg,'m--*')
pyplt.title('Second Derivative')

#print (df)
#    return df
