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
	
# Function to perform Convolution 	
def convolution():
	for i in range(len(x)):
		for j in range(len(h)):
			c[i+j]=c[i+j]+x[i]*h[j]	
	
	
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
	if sh1[i] !=sh1[i-1]+1:
		for k in range(sh1[i]-sh1[i-1]-1):  # inserting zero if some points are missing in x[n]
			sh1.insert(i+k,0)
			x.insert(i+k,0)
			n1=n1+1
	i=i+1+K		 

x1=min(sh1)
x2=max(sh1)	




print("Enter number of term in h[n] ")
n2=int(input())

print("Enter the element of h[n] (i.e first enter coeff of delta function and its shifted point on x-axis")
h=[]
sh2=[]
k=0
for i in range(n2):  #Taking input of impulse h[n]
	h.append(float(input()))  #storing coefficient
	sh2.append(int(input()))# storing shifted point
	if sh2[i] !=sh2[i-1]+1:
		for k in range(sh2[i]-sh2[i-1]-1):
			sh2.insert(i+k,0)	
			h.insert(i+k,0)
			n2=n2+1
	i=i+1+k		
		
xx=min(sh2[0],sh1[0])


c=[0 for i in range(len(h)*len(x))]   #list to store convolved value
			
convolution()	

#Plotting Convolution sum
print("Convolution Sum is :")
for j in range(len(x)+len(h)-1):
		print(c[j])
		delta(xx,c[j],-10,10)
		xx=xx+1
				


plt.grid()
plt.margins(0.1)
plt.show()


