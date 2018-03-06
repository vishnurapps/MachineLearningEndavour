#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 21:31:00 2018

@author: vishnu
"""

"""
In case of a mutiple linear regression, the equation can be written like this
y = b0 + b1x1 + b2x2 + ... + bnxn where y is the dependent variable and x is the 
independent variable.
"""

#Importing Libraries that are required for preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#Encoding categorical value
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [3])   #Here we specify the column to encode.
X = onehotencoder.fit_transform(X).toarray()    #After this we can see that the states are replaced by ones and zeros

