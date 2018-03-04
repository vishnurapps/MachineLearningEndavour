#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 22:46:48 2018

@author: vishnu
"""

#Importing Libraries that are required for preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing dataset
dataset = pd.read_csv('Data.csv')

"""
iloc stands for integer location, which is used for slicing the dataset
we can see [:, :-1] below which has a comma
what is on left of the comma is the rows and what is on right is column
: means we want all rows and :-1 means we need all but last column
values means we want to take the values
"""

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#How to handle missing data
from sklearn.preprocessing import Imputer

"""
missing_values means what we need to search for missing values in the dataset
strategy is the way we want to calculate the missing value we can use mean, median etc.
axis means how we want to calculate the mean along row or column
if axis is 0, then calculate along column if 1 calculate along row
"""

imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer.fit(X[:, 1:3])  #here we are telling the imputer where we want it to fit all rows and second and third column
X[:, 1:3] = imputer.transform(X[:, 1:3])    #here we are telling the imputer to do the mean to find missing values

#Encoding categorical value
from sklearn.preprocessing import LabelEncoder
 
"""
Here the first column is country name, we cannot use that in data processing
For the same, we need encode this to number. We are using LabelEncoder for that
"""
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])   #[0, 2, 1, 2, 1, 0, 2, 0, 1, 0] this is the value after conversion France=>0 Spain=>2 Germany=>1

"""
Machine learning is based on equations. As different countries are given different values there is a 
possible chance of misinterpretation. So we cannot use the values 0, 1 and 2 as replacement for country names.
We need to encode this again. To solve this issue we use the OneHotEncoder
"""
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])   #Here we specify the column to encode.
X = onehotencoder.fit_transform(X).toarray()    #Here the column 0 is replaced by 3 columns 0 => 100 1=>010 2=>001

"""
Encoding the dependent variable. Here we need to only use the LabelEncoder, because as it is a dependent variable,
the machine learning model knows that this is a catagory and there is no order between the two (yes and no)
"""
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)