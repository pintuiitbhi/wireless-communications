#Function for Plotting backward differencing system
import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
import cmath as cm
#Function for computing the DTFT
def dtft_func(x,n,N):
    j=cm.sqrt(-1)
    X=[]
    phase=[]#list of phase wrt w
    w=np.linspace(-np.pi,np.pi,N)
    for i in range(0,N):
        w_tmp=w[i]
        X_tmp=0
        for k in range(0,len(x)):
            X_tmp+=(x[k]*np.exp(-n[k]*w_tmp*j))

        phase.append(cm.phase(X_tmp))
        X.append(abs(X_tmp))
    return X,phase,w

# delta function
def delta(m):
    if m==0:
        return 1
    else:
        return 0
print("wait!!")
x=[]
M=8
n=np.linspace(-1000,1000,2001)
x.append(1)
x.append(-1)
D=dtft_func(x,n,100)
X=D[0]
theta=D[1]
w=D[2]

fig=plt.figure()
ax1=fig.add_subplot(211)
ax1.plot(w,X)
ax1.set_ylabel('$|X(e^{jw})|$')
ax1.set_xlabel('$w$')
plt.grid
ax2=fig.add_subplot(212,sharex=ax1)
ax2.plot(w,theta)
ax2.set_ylabel('$arg(X(e^{jw}))$')
ax2.set_xlabel('$w$')
plt.grid
plt.show()
