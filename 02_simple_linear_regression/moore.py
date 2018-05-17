#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 23:44:49 2018

@author: vishnu
"""

import re
import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

# some numbers show up as 1,170,000,000 (commas)
# some numbers have references in square brackets after them
non_decimal = re.compile(r'[^\d]+')

for line in open('moore.csv'):              #reading data from csv file
    r = line.split('\t')

    x = int(non_decimal.sub('', r[2].split('[')[0]))
    y = int(non_decimal.sub('', r[1].split('[')[0]))
    X.append(x)
    Y.append(y)


X = np.array(X)
Y = np.array(Y)

plt.scatter(X, Y)
plt.show()

Y = np.log(Y)                               #converting to log scale in X axis
plt.scatter(X, Y)
plt.show()

denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean()*X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

Yhat = a*X + b                              #Predicted value of Y

plt.scatter(X, Y)
plt.plot(X, Yhat, color='red')
plt.show()

d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)            #Accuracy of the model 0.9529
print("a:", a, "b:", b)                     #a = .0.351 b=-685.00
print("the r-squared is:", r2)

# how long does it take to double?
# log(transistorcount) = a*year + b
# transistorcount = exp(b) * exp(a*year)
# 2*transistorcount = 2 * exp(b) * exp(a*year) = exp(ln(2)) * exp(b) * exp(a * year) = exp(b) * exp(a * year + ln(2))
# a*year2 = a*year1 + ln2
# year2 = year1 + ln2/a
print("time to double:", np.log(2)/a, "years")      #1.974