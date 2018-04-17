'''

   File containing activation functions and their derivatives

'''

import numpy as np


'''
   Sigmoid activation function
   
   if needing the derivative, get that
   d/dx of sig is just sig(x)(1-sig(x))
'''
def sigmoid(x, dx=False):

   sig = lambda x: 1.0/(1.0+np.exp(-x))
   x = sig(x)

   if dx:
      return np.multiply(x, 1-x)

   return x
