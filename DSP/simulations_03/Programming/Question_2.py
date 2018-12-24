import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
import cmath as cm
#import scipy.fftpack as sf
from scipy.fftpack import fft, ifft


#x1 is a two dimensional list with one row as its value and
#other row as its domain point n of that value i.e. x1=[x,n]
def dtft(x1,N):
    #N=len(x)-1
    x=x1[0]
    j=cm.sqrt(-1)
    n=x1[1]
    X=[]
    theta=[]
    w=np.linspace(-np.pi,np.pi,N)
    for i in range(0,N):
        w_tmp=w[i]
        X_tmp=0
        for k in range(0,len(x)):
            X_tmp+=(x[k]*np.exp(-n[k]*w_tmp*j))

        theta.append(cm.phase(X_tmp))
        X.append(abs(X_tmp))
    return X,theta,w

#Example 2
def delta(m):
    if m==0:
        return 1
    else:
        return 0

x=[]
M=8
n=np.linspace(-499,500,1000)
for i in n:
    sum=0
    for k in range(0,M):
        sum=sum+delta(i-k)
    x.append(sum/M)
x1=[x,n]

D=dtft(x1,1000)
X=D[0]
theta=D[1]
w=D[2]

k=np.linspace(-499,500,1000)
dtft_x=abs(np.fft.fftshift(np.fft.fft(x)))

fig=plt.figure()
ax1=fig.add_subplot(311)
ax1.plot(k,X)
ax1.set_ylabel('$|X(e^{jw})|$')
ax1.set_xlabel('$w$')
ax1.title.set_text('The averaging system of length M=8')
plt.grid()

ax2=fig.add_subplot(312,sharex=ax1)
ax2.plot(k,dtft_x)
ax2.set_ylabel('$|X(e^{jw})|$')
ax2.set_xlabel('$w$')
plt.grid()
plt.show()
