
import  matplotlib.pyplot  as plt
import numpy as np
from scipy.io import wavfile
a=int(input("Enter 1-Male,2-Female"))
if a==1:
    file_name='brian.wav'
if a==2:
    file_name='amy.wav'
fs,data=wavfile.read(file_name)
a1=data[:,0]
a=a1[0:882]
w=np.linspace(-np.pi,np.pi,100)
#dtft
def dtft (a,w):
    N=np.linspace(0,881,882)
    X=[]
    for i in w:
        sum=0
        for k in N:
            temp=a[(int(k))]*np.exp(-1j*i*k)
            sum=sum+temp
        X.append(sum)
    return X
X=dtft(a,w)
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
