import numpy as nm

a=1.0
b=2.0
n=10
delta=(b-a)/n
x=nm.arange(a,b,delta)
y=x**2
tot=0.0
for i in range(len(x)):
    tot=tot+y[i]*delta

print tot
print 'error is ' + repr(tot-(b**3-a**3)/3.0)
