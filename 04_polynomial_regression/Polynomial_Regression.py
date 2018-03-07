#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:21:54 2018

@author: vishnu
"""

"""
Polynomial regression has equation of the form y = b0 + b1x + b2x^2 + ... + bnx^n
This is also called polynomial linear regression because, the coefficients of x's are linear
"""
#Importing Libraries that are required for preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing dataset
dataset = pd.read_csv('Position_Salaries.csv')

"""
Here the correct way to import the X here is X = dataset.iloc[:, 1].values But if we import
like this what we are going to get is a variable of type (10, ) which is a vector.
In machine learning, we want our input as matrix not as vector. So we are going to do a small 
trick. Instead of X = dataset.iloc[:, 1].values, we are going to give X = dataset.iloc[:, 1:2].values
Here the upper bound two will not be considered but we will get a matrix. If you check the size 
we can see that the size is (10,1) which is a 1D matrix.
"""

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

"""
To get a clear understanding on the differences between the linear and polynomial regression models,
we are going to implement both the models here.
"""

#Fitting the linear regression to dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

#Fitting the polymonial regression to dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 5)    #Highest degree of x

"""
We have only X here which is linear, we want coefficients of higher order of X. 
While creating the poly_reg, we specified that we want the square term as the highest order.
In that case we need the const term, coefficient of x and coefficient of x^2. X_poly contains
all those terms. To get X_poly we need to fit to X first and then transform.
"""
X_poly = poly_reg.fit_transform(X) 

"""
We are going to create one more linear regression object which is used to fit the X_poly.
There a possible doubt here. Why we need to fit again ? The reason is we have created a new
matrix of multiple columns using the polynomial regressor. We are fitting these columns 
with y.
"""

lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

#Visualising the Linear Regression Result
plt.scatter(X, y, color = "red")
plt.plot(X, lin_reg.predict(X), color = "blue")
plt.title("Truth or Bluff (Linear regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

#Visualising the Polynomial Regression Result

"""
Now coming into plotting the polynmial regression. How will we plot it ?
The thing that comes to our mind is replace the lin_reg with lin_reg_2. But will it solve the problem ?
If we look here, we can see that lin_reg_2 is an object of LinearRegression so
the replacement of the lin_reg with lin_reg_2 wont give us the desired result. 
So what if we replace X with X_poly ? X_poly is already created matrix from X, so 
if we get a new value to predect, using X_poly wont help us. So we have to use
 poly_reg.fit_transform(X)  instead of X_poly
 """
 
plt.scatter(X, y, color = "red")
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = "blue")
plt.title("Truth or Bluff (Polynomial regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()
