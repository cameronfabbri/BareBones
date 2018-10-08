import sys
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.linear_model import LinearRegression as LR

sys.path.insert(0, 'utils/')
from data_ops import Data

#from naiveBayes.naiveBayes import NaiveBayes
from linearRegression.linearRegression import LinearRegression

if __name__ == '__main__':

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

    lr = LinearRegression()
    lr.fit(train_X, train_y)
    
    reg = LR().fit(train_X, train_y)

    for x_,y_ in zip(test_X, test_y):
        print('Label :',y_)
        print('Pred  :',lr.predict(x_)[0])
        print('scikit:',reg.predict(x_.T.reshape(1,-1))[0])
        print()

