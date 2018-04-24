import numpy as np

data_dict = {
   'Yes':1,
   'No':0,
   'None':0,
   'Some':1,
   'Full':2,
   '$':0,
   '$$':1,
   '$$$':2,
   'French':0,
   'Thai':1,
   'Burger':2,
   'Italian':3,
   '0-10':0,
   '10-30':0,
   '30-60':0,
   '>60':0,
   }

'''
   Converts string data to numeric.
'''
def readData(filename):
   features = []
   labels   = []
   with open(filename) as f:
      for line in f:
         line    = line.rstrip().replace(' ','').split(',')
         print line
         line    = [data_dict[x] for x in line]
         feature = line[:-1]
         label   = line[-1]
         features.append(feature)
         labels.append(label)
   return features, labels

if __name__ == '__main__':

   features, labels = readData('restaurant.csv')

   i = 0
   for f in features:
      print str(f)+': '+str(labels[i])
      i += 1

