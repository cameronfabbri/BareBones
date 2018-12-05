'''
    Class to read in data
'''

import numpy as np

class Data(object):

    def __init__(self):

        self.data   = []
        self.target = []
        self.target_names = []

    '''
        Very simple 2 dimensional data for plotting purposes
    '''
    def load_simple(self):

        self.data = np.asarray([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5,\
            5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0])
        self.target = np.asarray([2.9, 2.7, 4.8, 5.3, 7.1, 7.6, 7.7, 7.6, 9.4, 9.0,\
            9.6, 10.0, 10.2, 9.7, 8.3, 8.4, 9.0, 8.3, 6.6, 6.7, 4.1])



    def load_iris(self, onehot=False):
        setosa     = 0
        versicolor = 1
        virginica  = 2

        if onehot:
            return NotImplementedError
        else:
            dummy = 0
            with open('utils/iris.csv', 'r') as f:
                for line in f:
                    line = line.rstrip().split(',')
                    if dummy == 0:
                        dummy = 1
                        continue
                    line[:-1] = np.asarray([float(i) for i in line[:-1]])
                    self.data.append(line[:-1])
                    if line[-1] == 'setosa': self.target.append(setosa)
                    if line[-1] == 'versicolor': self.target.append(versicolor)
                    if line[-1] == 'virginica': self.target.append(virginica)
        self.data = np.asarray(self.data)
        self.target = np.asarray(self.target)
        self.target_names = ['setosa', 'versicolor', 'virginica']

