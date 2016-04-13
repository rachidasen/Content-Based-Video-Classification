
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
    
 
       
 
 
def load_test_data(imsize=(200,200)):
    f=open("testing.pkl",'r')
    data=pickle.load(f)

    for image,i in data:
        im=cv2.imread(image)
        im=cv2.resize(im,imsize,interpolation = cv2.INTER_AREA)
        if not 'X_test' in locals():
            X_test=im[None,...]
        else:
            X_test=np.concatenate((X_train,im[None,...]), axis=0)  
        if not 'targets_test' in locals():
            targets_test=np.array([i])
        else:  
            targets_test=np.concatenate((targets_test,np.array([i])))
        
    testing={'x_test':X_test,'targets_test':targets_test}
    f=open('tesingdataset','wb')
    pickle.dump(testing,f,pickle.HIGHEST_PROTOCOL)
    f.close()
    del data
    
    
        
def load_val_data(imsize=(200,200)):
    f=open("validation.pkl",'r')
    data=pickle.load(f)
    sd=0
    for image,i in data:
        im=cv2.imread(image)
        im=cv2.resize(im,imsize,interpolation = cv2.INTER_AREA)
        if not 'X_val' in locals():
            X_val=im[None,...]
        else:
            X_val=np.concatenate((X_val,im[None,...]), axis=0)  
        if not 'targets_test' in locals():
            targets_val=np.array([i])
        else:  
            targets_val=np.concatenate((targets_val,np.array([i])))
        sd+=1
        print ("current image %d TOTAL %d")%(sd,len(data))
    validation={'x_val':X_val,'targets_val':targets_val}
    f=open('valdiationdataset','wb')
    pickle.dump(validation,f,pickle.HIGHEST_PROTOCOL)
    f.close()
    del data
    
   
 
 

    
    # time.sleep(secondsToSlep)
 
 
# Run following code when the program starts
if __name__ == '__main__':
  # load_Imagedata('frames')
  load_val_data()
