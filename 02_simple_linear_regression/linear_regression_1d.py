#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 23:16:35 2018

@author: vishnu
"""

import numpy as np
import matplotlib.pyplot as plt

X = []                              #lists to store data
Y = []
for line in open('data_1d.csv'):
    x, y = line.split(',')          #splitting the value of x and y from file
    X.append(float(x))              #adding data to the list X
    Y.append(float(y))              #adding data to the list Y

X = np.array(X)                     #converting X to numpy array
Y = np.array(Y)                     #converting Y to numpy array

plt.scatter(X, Y)                   #Plotting as a scatter plot
plt.show(X, Y)                      #Show the plot

denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean()*X.sum() ) / denominator               #slope of line
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator #y intercept


Yhat = a*X + b                      #predicted value of Y

plt.scatter(X, Y)
plt.plot(X, Yhat, color='red')      #plotting everything together
plt.show()

