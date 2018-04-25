import numpy as np


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


   def getImpurity(self):
      pass
   
   
   '''
      Creates a decision tree
   '''
   def fit(self, features, labels):

      '''
         go through each individual feature and count how many variations there
         are (boolean or not). Then count how many have yes, how many have no,
         and calculate impurity
      '''
      for feature in features.T:
         num_features = len(set(feature))
         print 'f:',feature
         print 'l:',labels

         # number of unique features
         num = len(set(feature))

         # need to count the number of pos/neg for each feature - create a matrix
         #     | f1 | f2 |
         # yes | 3  | 1  |
         # no  | 2  | 3  |
         
         data = np.zeros((2, num))

         print data
         for f in feature:
            for l in labels:
               if l == 0:
                  
                  data[f][0] += 1
                  print data
               elif l == 1:
                  data[f][1] +=1
                  print data
               print
         print data
         
         exit()
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

