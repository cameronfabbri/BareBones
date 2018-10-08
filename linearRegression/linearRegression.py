import numpy as np

class LinearRegression(object):


    def __init__(self, regularization=None):

        print('Initializing linear regression model...')

    def fit(self, X, y):
        self.W = np.expand_dims(np.matmul(np.linalg.inv(np.matmul(X.T, X)), np.matmul(X.T, y)),0)

    def predict(self, X):

        return np.matmul(self.W, X)
