#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 21:39:16 2018

@author: vishnu
"""

"""
K-Nearest Neighbours

This classifier is used when we have a scenario where we have few categories already 
present in our dataset. Now we have a new data point and we want to identify where this 
new data point belongs. This can be found out using the K-NN.

K-NN is performed in a number of steps.

Step 1 - Choose the number of K neighbours (default value is 5)
Step 2 - Take K nearest neighbours of the new data point according to the Euclidean distance
Step 3 - Amoung these K neighbours, count the number of data points in each category
Steo 4 - Assign the new data point to the category where you counted the most neighbors
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values     
y = dataset.iloc[:, 2].values 

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

## Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

