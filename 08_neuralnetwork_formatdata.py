# -*- coding: utf-8 -*-
# declaring utf8 encoding
# Example taken from EdoVaira/Iris-Neural-Network
# Dependencies
import os
import tensorflow as tf
import pandas as pd
import numpy as np

# Make results reproducible
seed = 1234
np.random.seed(seed)
tf.set_random_seed(seed)

# Loading the dataset
dataset = pd.read_csv('Iris_Dataset.csv')
dataset = pd.get_dummies(dataset, columns=['Species']) # One Hot Encoding
values = list(dataset.columns.values)

y = dataset[values[-3:]]
y = np.array(y, dtype='float32')
X = dataset[values[1:5]]
print X
X = np.array(X, dtype='float32')
print X

# Shuffle Data
indices = np.random.choice(len(X), len(X), replace=False)
X_values = X[indices]
y_values = y[indices]

# Creating a Train and a Test Dataset
test_size = 10
X_test = X_values[-test_size:]
X_train = X_values[:-test_size]
y_test = y_values[-test_size:]
y_train = y_values[:-test_size]

#check data
#print 'y_train', y_train
#print 'X_train', X_train
#print 'X_test', X_test
#print 'y_test', y_test

#print 'y_test', y_test[1]
