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
   '''
   def fit(self, features, labels):

      '''
         go through each individual feature and count how many variations there
         are (boolean or not). Then count how many have yes, how many have no,
         and calculate impurity
      '''

      # keep a dictionary of impurities for all features - pick smallest as root node
      impur = {}

      for feature in features.T:
         
         #print('f:',feature)
         #print('l:',labels)

         total = len(feature)
         numU  = len(set(feature))

         # create empty dictionary
         d = {}
         for f in set(feature):
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
         print()

      exit()

'''
class V(object):
   def __init__(self, f, num_t, num_f):
      self.f = f
      self.num_t = num_t
      self.num_f = num_f

   def increase(self, b):
      if b == 'positive':
         self.num_t += 1
      elif b == 'negative':
         self.num_f += 1
'''

class node(object):

   def __init__(self, value):
      self.value    = value
      self.positive = []
      self.negative = []
      self.children = []
      self.parent   = []
      self.root     = False
   
   def insertNode(self, obj):
      self.children.append(obj)

   def getChildren(self):
      return self.children


   


'''
d = decisionTree()
root = node(5)
root.insertNode(node(4))
print root.getChildren()[0].value
'''

