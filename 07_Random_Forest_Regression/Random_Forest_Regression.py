#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 23:33:20 2018

@author: vishnu
"""

"""
Random force is a version of ensemble learning. Ensemble learning is when you take multiple algorithms 
or the same algorithm multiple times and you put them together to make something much more powerful 
than the original. Out of all the data points we have, we are going to take K data points and 
we will build a decision tree based on that. In Random Forest Regression, we will plot so many 
decision trees and to predict the result, we will take the average of the prediction of all these 
decision trees
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values     #This is to get matrx as input. Explanation in polynomial regression
y = dataset.iloc[:, 2].values        

#Fitting Random Forest Regression to dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)      #n_estimators - Number of decision trees
regressor.fit(X,y)            

