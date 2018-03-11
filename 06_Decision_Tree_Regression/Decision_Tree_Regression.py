#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 11:38:05 2018

@author: vishnu
"""


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values     #This is to get matrx as input. Explanation in polynomial regression
y = dataset.iloc[:, 2].values                    

#Fitting Decision Tree Regression to dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

"""
On running the regression algorithm, it will start to split the data into various segments. 
The spliting is based on information entropy. The prediction in case of Decision Tree Regression 
is based on the average of the data in a particular segment
"""

#Visualising the dataset using decision tree regression
plt.plot(X, y, color = "red")
plt.scatter(X, regressor.predict(X), color = "blue")
plt.title("Truth or Bluff (Decision Tree Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

"""
What we have got above is not the real plot. Decision tree split the independent variable to 
different section based on entropy and information gained. We know that the decision tree is taking the average.
But the plot is not horizontal line. This is happening because of the resolution that
we are taking for plotting.

Here we are plotting the result at x = 1, 2, 3 etc only, not at any other points in between that.
To solve this what we need to do is, we need to increase the resolution of the graph
"""

#Explanation for bad plot
plt.scatter(X, y, color = "red")
plt.plot(X, regressor.predict(X), color = "blue")
plt.title("Truth or Bluff (Decision Tree Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()