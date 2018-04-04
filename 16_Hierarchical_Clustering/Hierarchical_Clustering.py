#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 22:13:13 2018

@author: vishnu
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

# Finding the optimal number of clusters using dentogram
import scipy.cluster.hierarchy as sch
dentogram = sch.dendrogram(sch.linkage(X, method = "ward"))
plt.title("Dentogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distances")
plt.show()