import numpy as np
from decisionTree import *

data_dict = {
   'Yes':1,
   'No':0,
   'None':0,
   'Some':1,
   'Full':2,
   '$':0,
   '$$':1,
   '$$$':2,
   'French':0,
   'Thai':1,
   'Burger':2,
   'Italian':3,
   '0-10':0,
   '10-30':1,
   '30-60':2,
   '>60':3,
   }

'''
   Converts string data to numeric.
'''
def readData(filename):
   features = []
   labels   = []
   with open(filename) as f:
      for line in f:
         line    = line.rstrip().replace(' ','').split(',')
         line    = [data_dict[x] for x in line]
         feature = line[:-1]
         label   = line[-1]
         features.append(feature)
         labels.append(label)
   return np.asarray(features), np.asarray(labels)

if __name__ == '__main__':

   features, labels = readData('restaurant.csv')

   features = np.asarray(features)
   labels = np.asarray(labels)

   d = decisionTree()
   print(features)
   print()
   exit()
   d.fit(features, labels)

   d.test(features, labels)

