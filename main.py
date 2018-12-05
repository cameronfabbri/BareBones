import sys
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import scipy.stats as stats

sys.path.insert(0, 'utils/')
from data_ops import Data
import measures

#from naiveBayes.naiveBayes import NaiveBayes
from linearRegression.linearRegression import LinearRegression

if __name__ == '__main__':

    #d = Data()
    #d.load_simple()
    #X = d.data
    #y = d.target
    
    iris = Data()
    iris.load_iris()
    X = iris.data
    y = iris.target
    
    # get a random train/test split
    num_data = len(y)
    train_num = math.floor(0.8*num_data)
    test_num = num_data - train_num
    # shuffle data
    c = list(zip(X,y))
    random.shuffle(c)
    X,y = zip(*c)

    train_X = np.asarray(X[:train_num])
    train_y = np.asarray(y[:train_num])
    test_X = np.asarray(X[train_num:])
    test_y = np.asarray(y[train_num:])

    ##### Linear Regression #####
    lr = LinearRegression()
    lr.fit(train_X, train_y)
    predictions = []
    for x_ in test_X:
        predictions.append(lr.predict(x_)[0])
    predictions = np.asarray(predictions)
    accuracy = measures.accuracy(predictions, test_y)
    print('Accuracy:',accuracy)
    ##### End Linear Regression #####
