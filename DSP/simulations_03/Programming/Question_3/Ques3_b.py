import matplotlib.pyplot as plt

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from numpy import pi,exp
def delta(n):
    if n==0:
        return 1
    else:
        return 0
a=int(input("Enter 1-Male,2-Female"))
if a==1:
    file_name='brian.wav'
if a==2:
    file_name='amy.wav'
fs,data=wavfile.read(file_name)
a1=data[:,0]
a=a1[0:882]
b=int(input("Enter 1-averaging function,2-backward differencing system"))
def avg(x):
    M=1
    for n in np.linspace(-1000,1000,2001):
        sum=0
        for k in range(0,M):
            sum=sum+delta(n-k)
        x.append(sum/M)
    return x
def back(x):
    for n in np.linspace(-1000,1000,2001):
        x.append(0.5*(delta(n) - delta(n-1)))
    return x
x=[]
if b==1:
    avg(x)
if b==2:
    back(x)
z=(np.convolve(x,a))
w=np.linspace(-pi,pi,100)

def dtft (z,w):
    N=np.linspace(0,2881,2882)
    X=[]
    for i in w:
        sum=0
        for k in N:
            temp=z[(int(k))]*exp(-1j*i*k)
            sum=sum+temp
        X.append(sum)
    return X
X=dtft(z,w)

fig=plt.figure()
ax1=fig.add_subplot(221)
ax1.plot(w,np.absolute(X),'r-')
ax1.set_ylabel('|X(jW)|')
ax1.set_xlabel('W')
plt.grid()
ax2=fig.add_subplot(222)
ax2.plot(w,np.angle(X),'k-')
ax2.set_ylabel('<(X(jW))')
ax2.set_xlabel('W')
plt.grid()
plt.show()
