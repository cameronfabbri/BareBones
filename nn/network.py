'''

   Neural Network class

'''

import numpy as np

class neuralNetwork(object):

   #def __init__(self, num_inputs, num_outputs):
   def __init__(self):
      self.layers = []


   def printNetwork(self):
      return NotImplementedError

   '''
      Adding a layer to the network
   '''
   def addLayer(self, layer, activation_fn=None):
      self.layers.append(layer)


   '''
      Trains the model
   '''
   def train(self, data, labels, learning_rate=1e-4, batch_size=1, epochs=2):
      network_out = self.forward(data)
      print(network_out)
      exit()


   '''
      Forward propagation through all layers
   '''
   def forward(self, x):

      # remember first 'layer' is just the input nodes
      out = x
      for layer in self.layers:
         
         if layer.weights is not None:
            out = np.matmul(out,layer.weights)
            print(out.shape)

      return out


   '''
      Passes data through the network and returns the network output
   '''
   def predict(self):
      pass
