import time
from random import randint
import time
import pickle
import numpy as np
import os
import sys
import glob
import cv2
import random
import matplotlib.pyplot as plt
import bob.io.base
 
bigdataset={}

def load_Imagedata(imagedir='frames', minNumSamplesPerClass=100, imsize=(200,200), p_train=0.6, p_val=0.2):
  print("load images")
  classes=('basketball','diving','horse_riding','soccer_juggling','swing','trampoline_jumping','walking','biking',
       'golf_swing','tennis_swing','volleyball_spiking');
# get the parent directory where this program is stored
  pkl=open('training.pkl','rb')
  total=pickle.load(pkl)
  print (len(total))
  dist=len(total)/ 19
  # for i in range()
  # bigdataset={}


  j=-1
  
  for i in range(len(total)):
      if((i)%dist==0):
          j+=1
          bigdataset["dataset"+str(j)]={}
          # j+=1
      bigdataset["dataset"+str(j)][total[i][0]]=total[i][1]
  for j in range(19):
      print ("len %d"%len(bigdataset['dataset'+str(j)].keys()),"Values %d"%len(bigdataset['dataset'+str(j)].values()))


  print ("Total no of files %d"%len(total))
  print (bigdataset.keys())
  print (len(bigdataset['dataset1'].keys()),"Values %d"%len(bigdataset['dataset1'].values()))
  print ("bigdatast keys")
  
  pkl=open('dataset_dic.pkl','wb')
  pickle.dump(bigdataset,pkl,pickle.HIGHEST_PROTOCOL)
  pkl.close()
  
  
  print('Main Terminating...')
  for key,elem in bigdataset.iteritems():
    print "writing dataset1 numpy array to file"
    if isinstance(elem,dict):
        sd=0
        for img,i in elem.iteritems():
            plt.figure(1)
            plt.subplot(211)
            im=cv2.imread(img)
            plt.imshow(im)
            # plt.show()
            # time.sleep(1)
            im=cv2.resize(im,(100,100),interpolation = cv2.INTER_AREA)
            plt.subplot(212)
            plt.imshow(im)
            plt.show()
            time.sleep(1)
            # plt.wait(600)
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
