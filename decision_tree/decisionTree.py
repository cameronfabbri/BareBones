import numpy as np


'''

   Class for a decision tree

   Want a train() or fit() method

'''
class decisionTree(object):

   def __init__(self, depth=4, method='classification'):
      self.depth  = depth
      self.method = method


   def isPure(node):
      pass

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

d = decisionTree()

root = node(5)

root.insertNode(node(4))


print root.getChildren()[0].value


