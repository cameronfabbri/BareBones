import numpy as np


'''

   Class for a decision tree

   Want a train() or fit() method

'''
class decisionTree(object):

   def __init__(self, depth=4):
      self.depth = depth


class node(object):

   def __init__(self):
      self.value    = ''
      self.positive = []
      self.negative = []

   


d = decisionTree()

print d.depth
