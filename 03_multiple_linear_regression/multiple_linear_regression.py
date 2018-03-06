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

"""
Sample encoding of catagorical values in dataset
 
State		Kerala		Punjab
Kerala----->1			0
Punjab----->0			1
Punjab----->0			1
Kerala----->1			0
Kerala----->1			0
Punjab----->0			1
 
Here after encoding, we have two columns, one for kerala and other for pubjab. when 
the state is Kerala, we put one under Kerala and 0 under Punjab and viseversa. 
But if we look closely we dont need two columns to represent these two states. 
Only the Kerala column is required, if its 1 then state is Kerala otherwise state is Punjab. 
Here the Punjab column is a Dummy variable column 
"""

#Dummy Variable Trap
X = X[:, 1:]    #Here we are removing the first column from the list

"""
Dummy Variable trap
In the case of the above example, we can see that the value of Punjab is always 1-Kerala. 
When we give the model these two columns as input, there is a chance that the model may 
consider these two as significant. But they are not. This is called the dummy variable trap. 
In order to avoid this issue, what we need to do is always omit one column. If we have 3 
dummy variables use only 2.
"""

#Spliting to test and training set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
