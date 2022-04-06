# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:20:03 2022

"""
import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000,2001,2002,2003,2004,2005,2006])
y = np.array([231.4, 216.1, 193.7, 142.8, 117.7, 94, 75.1])
t =  np.array([-3, -2, -1, 0, 1, 2, 3])
##ty = np.array([-694.2, -432.2, -193.7, 0, 117.7, 188, 225.3])
yt_original = np.array([244.7,214.1,183.5, 0, 122.3, 91.7, 61.1])

#Formula ty
ty = []
column4 = []
yearsColumn4 = []
for i in range(0,len(y)):
 if(i>0 and i < len(y)-1):   
  column3 = y[i-1]+y[i]+y[i+1] #Column 3 values
  column4.append(column3/3) #column4 values
  yearsColumn4.append(years[i]) #axis x to plot column4 results
 ty.append(y[i]*t[i]) #ty result when column4 is empty(first and last rows)
    

#Formula a0
sums = 0
for number in y:
    sums += number
a0 = sums/len(years)    

##Formula A1
sumYT = 0
for number in ty:
    sumYT += number
    
sumT2 = 0
for number in t:
    t2 = number*number #t^2
    sumT2 += t2
a1 = sumYT/sumT2  

##Formula Yt ->last column
yt = []
for i in range (0,len(y)):
 yt.append(a0+a1*t[i])

print('yt: ',yt)

############# 
#PLOT GRAPH 
#############
#GRID LINES
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) #CREATE A SUBPLOT

major_ticks = np.arange(50, 290, 40) #ARRAY WITH THE DESIRED NUMBERS

ax.set_ylim([40, 300]) #SET GRAPH Y-AXIS LIMITS
ax.set_yticks(major_ticks) 
ax.grid(axis='y') #PLOT GRIDS ONLY IN Y-AXIS

#Lines
ax.plot(years, yt,color='blue') #trend
ax.plot(yearsColumn4, column4,marker='o',color='orange') #column4
ax.plot(years, y, linestyle='-', marker='o',color='red') #y

#DESIGN
#ax.set_title('title')
ax.legend(['Линия тренда',
           'скользящая средняя\n по 3 годам',
           'число зарегистрированных\n в органах занятости\n в качестве безработных'],
          loc="upper right")
ax.set_xlabel('years')
#ax.set_ylabel('value')

#SHOW PLOT
plt.show()

print('MARCOS IS AWESOME😍 Лунита - королева😘')