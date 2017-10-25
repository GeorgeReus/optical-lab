# -*- coding: utf-8 -*-
"""
Created on Mon May 15 13:29:35 2017

@author: George
"""
'''
h=input("input the number of space:") #单元分割   1/h为步长
x=[]       #储存xi的列表
x0=0    #X0的值
for i in range(h):
    x0=x0+1.0/h
    x.append(x0)
rint(x)
'''
from scipy import integrate
import matplotlib.pyplot as plt
from math import sin
import numpy as np



x=[0,0.2,0.4,0.6,0.8,1.0]
h=5
#——————————基函数————————————————————————

def N2(x):     #  0<x<0.4
    if 0<=x<=0.2:
        return(x-0)/(1.0/h)
    elif 0.2<=x<=0.4:
        return(0.4-x)/(1.0/h)
    else:
        return 0.0
    
def N3(x):     #  0.2<x<0.6
    if x>0.2 and x<0.4:
        return (x-0.2)/(1.0/h)
    if x>0.4 and x<0.6:
        return (0.6-x)/(1.0/h)
    else:
        return 0
    
def N4(x):     #  0.4<x<0.8
    if x>0.4 and x<0.6:
        return (x-0.4)/(1.0/h)
    if x>0.6 and x<0.8:
        return (0.8-x)/(1.0/h)
    else:
        return 0
    
def N5(x):     #  0.6<x<1.0
    if x>0.6 and x<0.8:
        return (x-0.6)/(1.0/h)
    if x>0.8 and x<1.0:
        return (1.0-x)/(1.0/h)
    else:
        return 0
    
def N6(x): 
    if x>0.8 and x<1.0:    
        return (x-0.8)/(1.0/h)
    else:
        return 0

#—————————————————————————————————————————
def N22(x):
    y=N2(x)*N2(x)
    return y
    
k22,err=integrate.quad(N22,0,0.4)
k22=k22-25*0.4

def N33(x):
    y=N3(x)*N3(x)
    return y
k33,err=integrate.quad(N33,0.2,0.6)
k33=k33-25*0.4

def N44(x):
    y=N4(x)*N4(x)
    return y
k44,err=integrate.quad(N44,0.4,0.8)
k44=k44-25*0.4

def N55(x):
    y=N5(x)*N5(x)
    return y
k55,err=integrate.quad(N55,0.6,1.0)
k55=k55-25*0.4

def N23(x):
    y=N2(x)*N3(x)
    return y
k23,err=integrate.quad(N23,0.2,0.4)
k23=k23+25*0.2
k34=k45=k56=k23

'''def N32(x):
    y=N3(x)*N2(x)
    return y
k32,err=integrate.quad(N32,0.4,0.2)
k32=k32-25*0.2
k21=k43=k54=k32'''
k21=k32=k43=k54=k23

def b2_(x):
    y=N2(x)*(-x)
    return y
b2,err=integrate.quad(b2_,0,0.4)

def b3_(x):
    y=N3(x)*(-x)
    return y
b3,err=integrate.quad(b3_,0.2,0.6)

def b4_(x):
    y=N4(x)*(-x)
    return y
b4,err=integrate.quad(b4_,0.4,0.8)

def b5_(x):
    y=N5(x)*(-x)
    return y
b5,err=integrate.quad(b5_,0.6,1.0)
k=np.array([[1,0,0,0,0,0],[k21,k22,k23,0,0,0],[0,k32,k33,k34,0,0],[0,0,k43,k44,k45,0],[0,0,0,k54,k55,k56],[0,0,0,0,0,1]])
print(k)
b=np.array([0,b2,b3,b4,b5,0])
print(b)
y=np.linalg.solve(k,b)
print(y)
#——————————————————————————————————————————————————————————————
fig=plt.figure(figsize=(8,4))  
def u(x):
    y=np.sin(x)/sin(1.0)-x    #np.sin
    return y

plt.plot(x, y, color='b', linestyle='--', marker='o', label='FEM data') 
plt.title('FEM',fontsize=25)
plt.xlabel('x',fontsize=20)
plt.ylabel('u',fontsize=20)  
for i in range(6):
    plt.text(x[i],y[i],'u('+str(i)+')',color='red',fontsize=12)  
plt.figtext(0.1,0.92,'Hi~',color='green')  
plt.annotate('u by FEM',xy=(x[2],y[2]),xytext=(x[2],0.045),arrowprops=dict(facecolor='blue', shrink=0.1,headwidth=5,width=1),size=20) 
t=np.arange(0,1,0.01)
plt.plot(t,u(t),'m',linestyle='-', label='True data')
plt.legend(loc='upper left') 
plt.grid(True)
plt.savefig('FEM.jpg', format='jpg') 
plt.show()  
