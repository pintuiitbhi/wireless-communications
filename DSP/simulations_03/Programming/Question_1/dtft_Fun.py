
import matplotlib.pyplot as plt
import numpy as np
from sympy  import *
import cmath



n=np.linspace(-10,10,21)


print ("Enter the number of term in x[n]")
t=int(input())

x=[]
s=[]

#Taking input of the Discrete Signal
print("Enter the input discrete signal x[n], first coeff and then shift\n For example:\n for 2\delta[n-1] \nEnter:-\ncoeff shift \n2 1")
for i in range(t):
	a,b=input().split()
	x.append(float(a))
	s.append(int(b))
	k=0
	while s[i-1+k]!=s[i]-1:
		s.insert(i+k-1,s[i+k-1]+1)
		x.insert(i+k-1,0)
		k+=1

#Plotting the input signal
plt.stem(s,x)
plt.grid()
plt.margins(.1)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("Input Signal (Backward  differencing system) ")
plt.show()

w=symbols('w')  #Defining w as symbol for omega
X=0

#Finding the dtft
for i in range(len(x)):
	X=X+x[i]*exp(-w*s[i]*1j)

print(X)

#Taking samples of w
print("Enter samples of w")
s=int(input())
k=np.linspace(-np.pi,np.pi,s)


Y=[]
P=[]

#Calculating Magnitude and phase of DTFT
for i in range(s):
	
	P.append(cmath.phase(X.evalf(subs={w:k[i]})))
	Y.append(simplify(np.abs(X.evalf(subs={w:k[i]}))))
	

#Plotting the Magnitude
plt.plot(k,Y)
plt.margins(0.05)
plt.xlabel("$\omega$")
plt.ylabel("|(X(e$^j$$\omega$)|")
plt.title("Magnitude of X(e$^j$$^w$) (100 samples)")
plt.grid()
plt.show()

#Plotting the Phase
plt.plot(k,P)
plt.margins(0.05)
plt.xlabel("$\omega$")
plt.ylabel("Angle")
plt.title("Phase of X(e$^j$$^w$)(100 samples)")
plt.grid()
plt.show()



	
	
	
