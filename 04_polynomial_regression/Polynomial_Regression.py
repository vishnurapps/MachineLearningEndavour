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