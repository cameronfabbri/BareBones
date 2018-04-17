'''

   Neural Network class

'''


class neuralNetwork(object):

   #def __init__(self, num_inputs, num_outputs):
   def __init__(self):

      pass


   def printNetwork(self):
      return NotImplementedError

   '''
      Adding a layer to the network
   '''
   def addLayer(self, layer, activation_fn=None):

      pass


   '''
      Trains the model
   '''
   def train(self, data, labels, learning_rate=1e-4, batch_size=4, epochs=2):
      pass


   '''
      Passes data through the network and returns the network output
   '''
   def predict(self):
      pass
