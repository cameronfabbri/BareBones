from __future__ import division
from __future__ import absolute_import

import numpy as np
import math


'''

   Class for a decision tree

   Want a train() or fit() method

'''
class decisionTree(object):

   def __init__(self, depth=4, method='classification'):
      self.depth  = depth
      self.method = method


   def isPure(node, epsilon=1e-4):
      pass


   def getImpurity(self, d):
      # get total number of data points
      nm = 0.0
      for key in d:
         val1,val2 = d[key]
         nm = nm + val1 + val2

      impurity = 0.0
      for key in d:
         nmj = sum(d[key])
         outter = -(nmj/nm)
         inner  = 0.0
         for e in d[key]:
            if e == 0:
               outter = 0.0
               break
            inner = inner + (e/nmj)*math.log((e/nmj),2.0)

         impurity += outter*inner
         
      return impurity

   '''
      Creates a decision tree

      1. Find impurity for all remaining features
      2. Split on feature with least impurity
      3. 
   '''
   def fit(self, features, labels):

      # keep a dictionary of impurities for all features - pick smallest as root node
      impur = {}
      minImp = float('inf')

      for f_idx, feature in enumerate(features.T):
         
         total = len(feature)
         numU  = len(set(feature))
         featureVals = list(set(feature))

         # create empty dictionary
         d = {}
         for f in featureVals:
            d[f] = [0,0] # [T,F]

         # this dictionary contains the number of times each feature resulted in true
         for f,l in zip(feature, labels):
            # label is true
            if l == 1:
               v = d[f]
               v[0] += 1
               d[f] = v
            # label is false
            if l == 0:
               v = d[f]
               v[1] += 1
               d[f] = v

         impurity = self.getImpurity(d)
         print(impurity)

         impur[f_idx] = [impurity, feature]
         if impurity < minImp:
            minFeature = feature
            minImp = impurity
            minIdx = f_idx

      '''
         Now that we have the feature with the smallest impurity,
         we want to construct that as a node and split on that feature.
      '''
      print(minIdx)
      print(minFeature)
      print(minImp)

      # create a root node
      root = node()
      root.isRoot = True
      root.value = minIdx

      featureVals = list(set(minFeature))
      # for each featureVal, create a node and attach it to the root
      for fv in featureVals:
         n = node()
         n.edge = fv
         root.insertNode(n)

      print(root.getChildren())
      exit()




'''
   For all nodes, the value of the edge is stored in the parent
'''
class node(object):

   def __init__(self):
      self.children = []
      self.parent   = []
      self.isRoot   = False
      self.isLeaf   = False
      self.value    = None
      self.edge     = None

   def insertNode(self, obj):
      self.children.append(obj)

   def getChildren(self):
      return self.children

   

   
