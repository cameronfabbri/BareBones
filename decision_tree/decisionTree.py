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
      self.tree   = False

   def test(features, labels):
      return NotImplementedError

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
      Given features and labels, finds the feature to split on
   '''
   def findFeature(self, features, labels):
      # keep a dictionary of impurities for all features - pick smallest as root node
      impur = {}
      minImp = float('inf')
      for f_idx, feature in enumerate(features.T):
         total = len(feature)
         numU  = len(set(feature))
         featureVals = list(set(feature))
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
         impur[f_idx] = [impurity, feature]
         if impurity < minImp:
            minFeature = feature
            minImp     = impurity
            #minIdx     = f_idx
            minIdx = self.fdict[feature]
            print(minIdx)
            exit()
            minD       = d
      return minFeature, minImp, minIdx, minD

   def isTree(self):
      return self.tree
   
   def removeF(self, features, minIdx):
      start = features[:,:minIdx]
      end   = features[:,minIdx+1:]
      features = np.concatenate([start, end], axis=1)
      return features

   def buildTree(self, current_root, features, labels):

      minFeature, minImp, minIdx, minD = self.findFeature(features, labels)

      # remove the feature we decided to split on
      features = self.removeF(features, minIdx)

      if features.shape[1] == 1:
         print('no more features to split on')
         pass
      else:
         print('current_root:',current_root.value)

         # insert nodes into the tree
         for fv in current_root.branchValues:
            #print(minD[fv])
            n = Node()
            n.edge = fv
            if self.isPure(minD[fv]):
               n.isLeaf = True
               n.value = np.argmax(minD[fv])
               print('Node',n.value,'is pure, inserting as a leaf')
               current_root.insertNode(n)
            else:
               current_root.insertNode(n)
               n.value = minIdx
               current_root = n
               print('Node',n.value,'is NOT pure, inserting then recursing.')
               self.buildTree(current_root, features, labels)


   def fit(self, features, labels):

      # need to keep a dictionary of index:feature
      # because we delete things from the feature list

      # create a root node
      root = Node()
      root.isRoot = True

      # get the feature to split on first
      minFeature, minImp, minIdx, minD = self.findFeature(features, labels)
      root.value  = minIdx
      root.branchValues = list(set(minFeature))

      # now that we have a root node, need to recursively insert children
      self.buildTree(root, features, labels)

      #print(root.getChildren())
      print('Done!')
      exit()


# For all Nodes, the value of the edge is stored in the parent
class Node(object):

   def __init__(self):
      self.children = []
      self.parent   = []
      self.branchValues = []
      self.isRoot   = False
      self.isLeaf   = False
      self.value    = None # 0 or 1 if it is a leaf
      self.edge     = None

   def insertNode(self, obj):
      self.children.append(obj)

   def getChildren(self):
      return self.children

   def getParent(self):
      return self.parent

   
