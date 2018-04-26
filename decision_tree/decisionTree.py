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

   '''
      Checks if a node is pure or not up to some threshold epsilon
   '''
   def isPure(self, x, epsilon=1e-4):
      if min(x)/max(x) < epsilon: return True
      return False

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
            minImp     = impurity
            minIdx     = f_idx

            # here keep some info on the number of true/false so we can calculate if leaf
            minD = d

      print()
      '''
         Now that we have the feature with the smallest impurity,
         we want to construct that as a node and split on that feature.
      '''
      print('index:',minIdx)
      print('minFeature:',minFeature)
      print('impurity:',minImp)
      print('d:',minD)

      # create a root node - a node's value is the feature name
      root = Node()
      root.isRoot = True
      root.value  = minIdx

      # featureVals are numerical representations of the strings like None, Some, Full, etc
      featureVals = list(set(minFeature))
      # for each featureVal, create a node and attach it to the root
      for fv in featureVals:
         n = Node()
         n.edge = fv # set the edge to the feature value
         
         print(minD[fv])
         
         # if it's not a leaf, then we recurse on the feature that isn't a leaf
         if self.isPure(minD[fv]):
            print('node is pure')
         else: print('node is NOT pure')
         exit()

         root.insertNode(n)
         
      
      
      for n in root.getChildren():
         print(n.edge)
      exit()




'''
   For all Nodes, the value of the edge is stored in the parent
'''
class Node(object):

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

   

   
