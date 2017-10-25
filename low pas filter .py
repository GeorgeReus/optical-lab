# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:43:20 2017

@author: George
"""
import numpy as np
import matplotlib.pyplot as plt
X_22=[i for i in range(22,41)]
X_15=[i for i in range(15,30)]
X_32=[i for i in range(32,52)]
X_48= np.linspace(48,86,20)

Y_22_x1=[0.88,1.11,1.93,3.7,6.38,9.6,13,16.25,19.4,22.4,25.3,28,30.5,32.9,35.2,37.2,39.5,41.2,43]
Y_22_x2=[1.5,2.1,2.8,6.5,14.9,22.8,29.5,35,39.7,43.5,46.5,49.3,50.2,49.5,41.2,53.2,60.2,62.5,62.5]

Y_15_x1=[0.51,0.9,2.3,5.6,10.2,14.8,19.3,23.4,27.1,30.4,33.7,36.6,39.2,41.9,44.3]
Y_15_x2=[1.27,1.72,3.9,13.8,24,32.2,38.8,44.1,47.6,50,47,53.2,61,62.5,62.5]

Y_32_x1=[0.75,1.1,1.7,3.0,4.9,7.2,9.7,12.3,14.8,17.2,19.7,21.8,23.9,25.9,27.7,29.5,31.2,32.8,34.4,36]
Y_32_x2=[1.2,2.2,4.0,5.58,5.48,4.5,13.5,23.3,30.7,37,42,47.1,51,54.5,58,59,61.5,62.5,62.5,62.5]

Y_48_x1=[0.7,0.87,1.4,2.6,4.7,7.6,10.6,13.7,16.7,19.5,22.2,24.7,27.2,29.5,31.5,33.5,35.5,37.2,38.8,40.2]
Y_48_x2=[1.04,1.5,2.9,5.0,5.7,5.2,15.6,26.2,34.4,42,47.2,51.2,56,59,62,62.5,62.5,62.5,62.5,62.5]

plt.plot(X_22,Y_22_x1,color='b',label='one fiter')
plt.plot(X_22,Y_22_x2,color='m',label='two series filters')
plt.legend(loc='upper left') 
plt.grid(True)
plt.title('22MHz lowpass filter')
plt.xlabel('Frequency/MHz')
plt.ylabel('Loss/dB')
plt.show()
#
plt.plot(X_15,Y_15_x1,color='b',label='one fiter')
plt.plot(X_15,Y_15_x2,color='m',label='two series filters')
plt.legend(loc='upper left') 
plt.grid(True)
plt.title('15MHz lowpass filter')
plt.xlabel('Frequency/MHz')
plt.ylabel('Loss/dB')
plt.show()
#
plt.plot(X_32,Y_32_x1,color='b',label='one fiter')
plt.plot(X_32,Y_32_x2,color='m',label='two series filters')
plt.legend(loc='upper left') 
plt.grid(True)
plt.title('32MHz lowpass filter')
plt.xlabel('Frequency/MHz')
plt.ylabel('Loss/dB')
plt.show()
#
plt.plot(X_48,Y_48_x1,color='b',label='one fiter')
plt.plot(X_48,Y_48_x2,color='m',label='two series filters')
plt.legend(loc='upper left') 
plt.grid(True)
plt.title('48MHz lowpass filter')
plt.xlabel('Frequency/MHz')
plt.ylabel('Loss/dB')
plt.show()