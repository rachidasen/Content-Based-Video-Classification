
from random import randint
import time
import pickle
import numpy as np
import os
import sys
import glob
import cv2
import random
import bob.io.base
 
bigdataset={}

def load_Imagedata(imagedir='frames', minNumSamplesPerClass=100, imsize=(200,200), p_train=0.6, p_val=0.2):
  f=open("dataset_dic.pkl","rb")
  bigdataset=pickle.load(f)

  
  f.close()

  skip=['dataset17','dataset9','dataset18']

  for key,elem in bigdataset.iteritems():
    
    if isinstance(elem,dict) and key in skip:
      print "writing %s numpy array to file"%(key)
      sd=0
      for img,i in elem.iteritems():
        im=cv2.imread(img)
        im=cv2.resize(im,imsize,interpolation = cv2.INTER_AREA)
        print "category %d curent %d total %d"%(i,sd,len(elem.keys()))           
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
      print "X_train_shape",X_train.shape

      targets_train=targets_train.astype(np.int32)


      
      file_name='X_train'+key+'.hdf5'
      print file_name
      fa = bob.io.base.HDF5File(file_name, 'a')
      fa.set('frame',X_train)
      del fa

      pkl2=open('Y_train'+key+'.pkl','wb')
      pickle.dump(targets_train,pkl2,pickle.HIGHEST_PROTOCOL)
      pkl2.close()
      print ("1 file written")
      del targets_train
 
      del X_train        
    
 
       
 
 
 
   
 
 

    
    # time.sleep(secondsToSlep)
 
 
# Run following code when the program starts
if __name__ == '__main__':
  load_Imagedata('frames')
