import numpy as np
from matplotlib import pyplot as plt
import math
import time

def gauss(x,x0=0,sigma=1,amp=1):
    #a*e^(-(x-x0)^2/2sigma^2)
    y=amp*np.exp(-(x-x0)**2/2/sigma**2)
    return y

x=np.arange(-5,5,0.0001)
t1=time.time()
y=gauss(x,amp=2)
t2=time.time()
y2=slow_gauss(x,amp=2)
t3=time.time()
print t3-t2
print t2-t1
plt.ion()
plt.plot(x,y)
#plt.show()
