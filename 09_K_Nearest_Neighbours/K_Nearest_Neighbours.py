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