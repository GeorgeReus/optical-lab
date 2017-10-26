# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:46:51 2017

@author: George
"""
import heapq # 找数据中的几个最大值或最小值
import pylab as plt
import numpy as np
import pandas as pd
data=np.loadtxt(r'D:\microwave data\20171011\SPEC-20171011-161+115  20ILP-4.txt')   #数据文件地址
i=3 #取几个最大值
data1=data[:,0]   #第一列  波长
data2=data[:,1]   #第二列 幅值

plt.plot(data1,data2,color='b') 
plt.grid(True)


plt.annotate('f1=1555.88',xy=(1555.88,-53.543),xytext=(1555.88,-30),arrowprops=dict(facecolor='blue', shrink=0.1,headwidth=5,width=1),size=15) 
plt.annotate('f2=1559.52',xy=(1559.52,-53.543),xytext=(1559.52,-75),arrowprops=dict(facecolor='blue', shrink=0.1,headwidth=5,width=1),size=15) 
plt.annotate('f3=1562.74',xy=(1562.74,-53.543),xytext=(1562.74,-30),arrowprops=dict(facecolor='blue', shrink=0.1,headwidth=5,width=1),size=15) 
plt.annotate('f4=1566.74',xy=(1566.74,-53.543),xytext=(1566.74,-30),arrowprops=dict(facecolor='blue', shrink=0.1,headwidth=5,width=1),size=15) 
 
plt.title('20 deg ILP 161+115 ',fontsize=25)
plt.xlabel('wavelength/nm',fontsize=20)
plt.ylabel('intensity/dBm',fontsize=20)
plt.show()
parameters=[]
data3=pd.Series(data2,index=data1)
parameters=heapq.nlargest(i, data3) #找最大的几个值

      
  
