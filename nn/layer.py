import numpy as np
import activation_functions as ac

class Layer(object):

   def __init__(self, num_nodes, previous_layer=None, input_=False, output_=False, name=None, verbose=False, activation=ac.sigmoid):

      self.num_nodes = num_nodes
      self.name      = name
      self.weights   = None
      self.bias      = None
      self.activation = activation

      # define initial weights if not an input layer

      if not input_:

         if verbose:
            print('creating initial weights for ' + name)
            print('previous layer nodes:',previous_layer.num_nodes)
            print('current layer nodes:',self.num_nodes)


         # TODO need to remember bias
         
         # weight matrix will be of size previous_layer.num_nodes x self.num_nodes
         self.weights = np.random.randn(previous_layer.num_nodes,self.num_nodes)

      # define biases
      self.bias = np.ones(self.num_nodes)
      print(self.bias.shape)
      exit()


