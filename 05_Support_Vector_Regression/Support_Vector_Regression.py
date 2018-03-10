#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 23:16:46 2018

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
y = np.array(y).reshape(-1,1)                     #Explanation of numpy reshape is available as a jupiter notebook.

"""
In the previous sections other than preprocessing section, we didnt do feature scaling.
That was because, the libraries that we were using was doing the same internally. But in 
case of the library that we are using for SVR,feature scaling is not done by default. So 
we have to do the same.
"""

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = np.ravel(sc_y.fit_transform(y))


#Fitting SVR to dataset
from sklearn.svm import SVR

"""
There are types of kernels in SVR. Our problem is non linear. We are going to use rbf kernel here.
"""
 
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

#Visualising the SVR result
plt.scatter(X, y, color = "red")
plt.plot(X, regressor.predict(X), color = "blue")
plt.title("Truth or Bluff (SVR)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

"""
If we see the plot, we can see that the there is a big mismatch between the real and predicted salary of CEO.
This is because SVR consider it as an outlier. The model was made to fit to other data points.
"""


#Predcting the result

"""
Here we cannot add 6.5 as input to the transform method, because it is expecting a matrix as input.
To convert 6.5 to array we use numpy.array[[6.5]]. First square bracket is used to represent all rows of the
matrix and second bracket to represent each row. We are doing the transform and inverse transform as we have done 
feature scaling to the orginal data fed to the model.
"""

y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))

