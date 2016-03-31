from threading import Thread
from random import randint
import time
import cPickle as pickle
import numpy as np
import os
import sys
import glob
import cv2
import random
 
bigdataset={}

def load_Imagedata(imagedir='frames', minNumSamplesPerClass=100, imsize=(200,200), p_train=0.6, p_val=0.2):
  print("load images")
  classes=('basketball','diving','horse_riding','soccer_juggling','swing','trampoline_jumping','walking','biking',
       'golf_swing','tennis_swing','volleyball_spiking');
# get the parent directory where this program is stored
  pkl=open('training.pkl','rb')
  total=pickle.load(pkl)
  print len(total)
  dist=len(total)/21
  # for i in range()
  # bigdataset={}


  j=-1
  
  for i in xrange(len(total)):
      if((i)%dist==0):
          j+=1
          bigdataset["dataset"+str(j)]={}
          # j+=1
      bigdataset["dataset"+str(j)][total[i][0]]=total[i][1]
  for j in range(11):
      print "len %d"%len(bigdataset['dataset'+str(j)].keys()),"Values %d"%len(bigdataset['dataset'+str(j)].values())


  print "Total no of files %d"%len(total)
  print bigdataset.keys()
  print len(bigdataset['dataset1'].keys()),"Values %d"%len(bigdataset['dataset1'].values())
  print "bigdatast keys",
  # for keys in bigdataset:
  #   print keys
  #   print bigdataset[keys]
   
  # sd=0
  pkl=open('dataset_dic.pkl','wb')
  pickle.dump(bigdataset,pkl,pickle.HIGHEST_PROTOCOL)
  pkl.close()
  # for key,elem in bigdataset.iteritems():
  #    print "writing dataset1 numpy array to file"
  myThreadOb1 = MyThread(0)
  myThreadOb1.setName('Thread 1')
 
  myThreadOb2 = MyThread(7)
  myThreadOb2.setName('Thread 2')
 
  myThreadOb3 = MyThread(14)
  myThreadOb3.setName('Thread 3')
 
  
 
  # Start running the threads!
  myThreadOb1.start()
  myThreadOb2.start()
  myThreadOb3.start()
  
 
  # Wait for the threads to finish...
  myThreadOb1.join()
  myThreadOb2.join()
  myThreadOb3.join()
  
  print('Main Terminating...')
 
       
 
 
 
   
 
 
class MyThread(Thread):
 
  def __init__(self, key):
    ''' Constructor. '''
    Thread.__init__(self)
    self.key = key
    # self.elem={}
    self.elem = bigdataset['dataset'+str(key)]
 
 
  def run(self):
    
    for loop in range(7):
      key='dataset'+str(self.key)
      if isinstance(self.elem,dict):
        sd=0
        for img,i in self.elem.iteritems():
            # print img,i
          im=cv2.imread(img)
          im=cv2.resize(im,(150,150),interpolation = cv2.INTER_AREA)
          print "dataset %d curent %d total %d"%(self.key,sd,len(self.elem.keys()))            
          rs=random.random()
          if not 'X_train' in locals():
                  X_train=im[None,...]
          else:
            X_train=np.concatenate((X_train,im[None,...]), axis=0)      
          if not 'targets_train' in locals():
            targets_train=np.array([i])
          else:  
            targets_train=np.concatenate((targets_train,np.array([i])))
         
          sd+=1
 
            
       
        #typecast targets
       
        targets_train=targets_train.astype(np.int32)
 
 
        # apply some very simple normalization to the data
        X_train=X_train.astype(np.float32)
 
        X_train -= X_train.mean()
        # X_train /= X_train.std()
 
        # batch={'X_train':X_train,'targets_train':targets_train,'X_val':X_val,'targets_val':targets_val,'X_test':X_test,'targets_test':targets_test}
        pkl=open('X_train'+key+'.pkl','wb')
        pickle.dump(X_train,pkl,pickle.HIGHEST_PROTOCOL)
        pkl.close()
 
        pkl=open('Y_train'+key+'.pkl','wb')
        pickle.dump(targets_train,pkl,pickle.HIGHEST_PROTOCOL)
        pkl.close()
        print "1 file written"
        del targets_train
   
        del X_train        
      self.key+=1
    # time.sleep(secondsToSlep)
 
 
# Run following code when the program starts
if __name__ == '__main__':
  load_Imagedata('frames')