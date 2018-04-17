import numpy as np

class Layer(object):

   def __init__(self, num_nodes, previous_layer=None, input_=False, output_=False, name=None):

      self.num_nodes = num_nodes
      self.name      = name
      self.weights   = None


      # define initial weights if not an input layer

      if not input_:

         print 'creating initial weights for ' + name
         print previous_layer.num_nodes
         print self.num_nodes


         # TODO need to remember bias
         
         # weight matrix will be of size previous_layer.num_nodes x self.num_nodes
         self.weights = np.random.randn(previous_layer.num_nodes,self.num_nodes)
         print self.weights
         exit()


