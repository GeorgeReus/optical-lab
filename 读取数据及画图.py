# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 21:58:03 2017

@author: George
"""

import pylab as plt
import numpy as np
data=np.loadtxt(r'D:\microwave data\Freq-20171017-yin_2017_1017.txt')   #数据文件地址
data1=data[5:,1]  # f1
data2=data[5:,2]  # f2
data3=data[5:,3]  # △f
m=data1.shape[0]

x=range(0,m)
x=np.array(x)
x=x*0.5/10 #换算成μs
data1_mean=data1.mean()
data1_mean=data1_mean/1e6
data2_mean=data2.mean()
data2_mean=data2_mean/1e6
#均方差
data1_std=np.std(data1)
print('f1_std='+str(data1_std))
data2_std=np.std(data2)
print('f2_std='+str(data2_std))
data3_std=np.std(data3)
print('△f_std='+str(data3_std))


#画 双波长频率 f1  
plt.plot(x,data1,color='b',label='f1_mean=4'+str(data1_mean)+'MHz')
plt.annotate('f1_max=40.561009MHz',xy=(30.6328,561009),xytext=(7.3,561006),arrowprops=dict(facecolor='blue', shrink=0.1,headwidth=5,width=1),size=20)
plt.annotate('f1_min=40.560960MHz',xy=(3.17124,560960),xytext=(17.4123,560964),arrowprops=dict(facecolor='blue', shrink=0.1,headwidth=5,width=1),size=20)
plt.legend(loc='upper right',fontsize=25) 
plt.grid(True)
plt.title('f1 of Dual_wavelength mode-locked fiber laser',fontsize=25)
plt.xlabel('t/microsecond',fontsize=20)
plt.ylabel('Frequency/MHz +40MHz.',fontsize=20)
plt.show()

#画 双波长频率  f2

plt.plot(x,data2,color='m',label='f2_mean=4'+str(data2_mean)+'MHz')
plt.annotate('f2_max=40.563254MHz',xy=(30.6466,563254),xytext=(6.8164,563252),arrowprops=dict(facecolor='blue', shrink=0.1,headwidth=5,width=1),size=20)
plt.annotate('f2_min=40.563215MHz',xy=(3.17124,563215),xytext=(20.845,563218),arrowprops=dict(facecolor='blue', shrink=0.1,headwidth=5,width=1),size=20)
plt.legend(loc='upper right',fontsize=25) 
plt.grid(True)
plt.title('f2 of Dual_wavelength mode-locked fiber laser',fontsize=25)
plt.xlabel('t/microsecond',fontsize=20)
plt.ylabel('Frequency/MHz +40MHz',fontsize=20)
plt.show()

#画 双波长频率 f1  f2
plt.plot(x,data1,color='b',label='f1_mean=4'+str(data1_mean)+'MHz')
plt.plot(x,data2,color='m',label='f2_mean=4'+str(data2_mean)+'MHz')
plt.legend(loc='upper right',fontsize=25) 
plt.grid(True)
plt.title('Dual-wavelength mode-locked fiber laser Frequency',fontsize=25)
plt.xlabel('t/microsecond',fontsize=20)
plt.ylabel('Frequency/MHz',fontsize=20)
plt.show()

# 画 频差△f
data3_mean=data3.mean()
plt.plot(x,data3,color='b',label='Frequency Difference mean='+str(data3_mean)+'Hz')
plt.legend(loc='upper right',fontsize=25) 
plt.title('Dual-wavelength mode-locked fiber laser Frequency Difference',fontsize=25)
plt.grid(True)
plt.xlabel('t/microsecond',fontsize=20)
plt.ylabel('Frequency Difference/Hz',fontsize=20)
plt.show()