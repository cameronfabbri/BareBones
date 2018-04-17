import numpy as np

class Layer(object):

   def __init__(self, num_nodes, previous_layer=None, input_=False, output_=False, name=None):

      self.num_nodes = num_nodes
      self.name      = name


      # define initial weights if not an input layer

      if not input_:
         print 'creating initial weights for ' + name
         exit()


