# -*- coding: utf-8 -*-
"""Ananda Fitri Karimah (1301170774)_IF-41-11_Random Walk.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VBAOVKCQmhpq17xdAvZLoEBdCQ_RYLM2
"""

# Python code for 2D random walk.
import random                         #for generate random number
from matplotlib import pyplot as plt  #for plot to the graph

#defining iteration and particle
n_partikel = 10                       #there is 10 particle
n_iterasi = 100                       #there is 100 steps

#defining xmax, xmin, ymax, ymin, xrange, and yrange 
x_max = 100                           #maximal axis x = 100 
x_min = -100                          #minimal axis x = -100
x_range = x_max - x_min               #the range is = 100 - (-100) = 200 

y_max = 100                           #maximal axis x = 100 
y_min = -100                          #minimal axis x = -100
y_range = y_max - y_min               #the range is = 100 - (-100) = 200

#creating two array for containing x and y coordinate  
xfin = [[0,0,0,0,0,0,0,0,0,0]]        #first condition for x final posisition is zero (0)
yfin = [[0,0,0,0,0,0,0,0,0,0]]        #first condition for y final posisition is zero (0)

# looping in range n_iterasi
for i in range (n_iterasi):
  tempx = []                          #make list for temporary x before go to the final list
  tempy = []                          #make list for temporary x before go to the final list
  # looping in range n_partikel
  for j in range(n_partikel):
      x = xfin [i][j]                 #calculate x [i][j]
      y = yfin [i][j]                 #calculate y [i][j]
      val = random.uniform(1, 0)      #generate random number for decision  
      
      #Update position
      #right position
      if val <= 0.25: 
          x = x + 1
      #left position
      elif val <= 0.50:
          y = y - 1 
      #up position
      elif val <= 0.75: 
          x = x - 1
      #down position
      else: 
          y = y + 1

      #PBC
      if (x > x_max) :
        x = x - x_range
      if (x < x_min) :
        x = x + x_range  

      if (y > y_max) :
        y = y - y_range
      if (y < y_min)  :
        y = y + y_range

      #appnend to temp
      tempx.append(x)
      tempy.append(y)

  #append to list final
  xfin.append(tempx)
  yfin.append(tempy)

#show the plot
plt.title("Random Walk ($n = " + str(n_iterasi) + "$ steps)")
plt.plot(xfin, yfin)
plt.show()

