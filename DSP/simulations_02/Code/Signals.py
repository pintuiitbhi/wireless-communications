import numpy as np
import matplotlib.pyplot as plt

# Defining Delta function to plot ( shifted to n0 and scaled with s)
def delta(n0,s,n1,n2):   # n1 and n2 is the lower and upper limit of x -axis
	if (n0<n1) or (n0>n2) or (n1>n2) :
		print ("Argument must be n1<=n0<=n2")
		return
		
	x=np.linspace(n1,n2,n2-n1+1)
	y= [0 for i in x]
	y[n0-n1]=s
	plt.stem(x,y,)
	plt.xlim([n1-1,n2+1])
	
	
print("Enter number of term  in x[n] ")
n1=int(input())

print("Enter the element of x[n] (i.e first enter coeff of delta function and its shifted point on x-axis")
x=[]

sh1=[]
K=0

# Taking input of x[n]
for i in range(n1):
	x.append(float(input()))  #storing the coefficient of delta term 
	sh1.append(int(input()))   #storing shifted point on x-axis
	delta(sh1[i],x[i],-10,10)	 #Plotting signal

plt.grid()

plt.margins(0.1)
plt.show()


