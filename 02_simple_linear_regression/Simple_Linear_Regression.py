#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 22:31:06 2018

@author: vishnu
"""

"""
Simple linear regression deals with equations of the form y = b0 + b1x, where b0 is the y intercept 
and b1 is the slope of the line. Here y is the dependent variable and x is the independent variable
The best fit line is calculated using the Ordinary Least Squares. Best fit line is the line having the 
smallest Ordinary Least Squares.
"""
#Importing Libraries that are required for preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#Splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

#Fitting simple linear regression to training set
from sklearn.linear_model import LinearRegression

#Here the simple linear regression model learns our data. The machine name is regressor, which is of type Simple Linear Regression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predecting the test results
y_pred = regressor.predict(X_test)

#Visualising the training set data
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, regressor.predict(X_train), color = "blue")
plt.title("Salary vs Experience (Train data)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

#Visualising the test set data
plt.scatter(X_test, y_test, color = "red")
plt.plot(X_train, regressor.predict(X_train), color = "blue")
plt.title("Salary vs Experience (Test data)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

