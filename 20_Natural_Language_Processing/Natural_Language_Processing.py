#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:37:16 2018

@author: vishnu
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = "\t", quoting = 3) #quoting = 3 is given to avoid double quotes

# Cleaning the text
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')   #contain the list of irrelevent letters
corpus =[]
for i in range (0, 1000):
    ps = PorterStemmer() #object used for stemming
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) # this is to remove everything other than characters and replace that by space
    review = review.lower() #convert to lower case
    review = review.split() #split the sentense to words
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))] #applying steming
    review = ' '.join(review) #making it a sentence again
    corpus.append(review) #adding to list
    
# Create a Bag of words model
from sklearn.feature_extraction.text import CountVectorizer
#cv = CountVectorizer()  #When we do like this it will take all unique words that the model sees in the review. We dont need all of them some might be a name or somethink like that
cv = CountVectorizer(max_features=1500) #Here we are saying that we need only the most relivent 1500 words
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values


