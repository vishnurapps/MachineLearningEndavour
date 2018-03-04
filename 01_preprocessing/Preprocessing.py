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
'''iloc stands for integer location, which is used for slicing the dataset
we can see [:, :-1] below which has a comma
what is on left of the comma is the rows and what is on right is column
: means we want all rows and :-1 means we need all but last column
values means we want to take the values'''
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values