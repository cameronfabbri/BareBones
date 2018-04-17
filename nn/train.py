'''

   Three layer neural network in numpy

'''

import numpy as np
import requests
import pickle
import gzip
import os

# import my nn class
from network import neuralNetwork as nn
from layer import Layer

def download():
   # mnist data in gz format
   url = 'http://deeplearning.net/data/mnist/mnist.pkl.gz'

   print 'Downloading mnist...'
   with open('mnist.pkl.gz', 'wb') as f:
      r = requests.get(url)
      if r.status_code == 200:
         f.write(r.content)
      else:
         print 'Could not connect to ', url

if __name__ == '__main__':

   # first get/load mnist
   #try:
   #   print 'Loading mnist'
   #   f = gzip.open('mnist.pkl.gz', 'rb')
   #   train_set, val_set, test_set = pickle.load(f)
   #except: download()

   # initialize an empty network
   #network = nn(784, 10)

   # dummy data
   data = np.asarray([[0,1], [1,0], [1,1], [0,0]])
   labels = np.asarray([[1], [1], [0], [0]])
   
   network = nn()

   # define the layers
   input_layer   = Layer(2, input_=True, name='input_layer')
   hidden_layer1 = Layer(2, name='hidden_layer1')
   output_layer  = Layer(1, output_=True, name='output_layer')

   # add layers to the network
   network.addLayer(input_layer)
   network.addLayer(hidden_layer)
   network.addLayer(output_layer)




   exit()

   network.train(data, labels)





