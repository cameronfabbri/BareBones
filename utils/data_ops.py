'''
    Class to read in data
'''

import numpy as np

class Data(object):

    def __init__(self):

        self.data   = []
        self.target = []
        self.target_names = []

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

