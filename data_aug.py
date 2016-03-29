import cPickle as pickle
import numpy as np
import os
import sys
import glob
import cv2
import random

def load_Imagedata(imagedir='frames', minNumSamplesPerClass=100, imsize=(200,200), p_train=0.6, p_val=0.2):
    print("load images")
    classes=('basketball','diving','horse_riding','soccer_juggling','swing','trampoline_jumping','walking','biking',
         'golf_swing','tennis_swing','volleyball_spiking');
# get the parent directory where this program is stored
    total=[]
    dataset={}
    # imagedir=os.path.join(os.getcwd(),imagedir)
    for i,category in enumerate(classes):
        #print "category %d" %i
        path=os.path.join(imagedir,category)
        # print path
        files=glob.glob(path+"/**/**/*.bmp")
        # print files
        
            #load the images one-by-one
        print "category %d len %d"%(i,len(files))
        total=total+files
        for f in files:
            dataset[f]=i
    # print total
    random.shuffle(total)
    random.shuffle(total)
    random.shuffle(total)
    random.shuffle(total)
    dist=len(total)/11
    j=-1
    bigdataset={}
    for i in xrange(len(total)):
        if((i)%dist==0):
            j+=1
            bigdataset["dataset"+str(j)]={}
            # j+=1
        bigdataset["dataset"+str(j)][total[i]]=dataset[total[i]]
    for j in range(11):
        print "len %d"%len(bigdataset['dataset'+str(j)].keys()),"Values %d"%len(bigdataset['dataset'+str(j)].values())


    print "Total no of files %d"%len(total)
    print bigdataset.keys()
    print len(bigdataset['dataset1'].keys()),"Values %d"%len(bigdataset['dataset1'].values())
    # sd=0
    pkl=open('dataset_dic.pkl','wb')
    pickle.dump(bigdataset,pkl,pickle.HIGHEST_PROTOCOL)
    pkl.close()
    for key,elem in bigdataset.iteritems():
        print "writing dataset1 numpy array to file"
        if isinstance(elem,dict):
            sd=0
            for img,i in elem.iteritems():
                im=cv2.imread(img)
                im=cv2.resize(im,imsize,interpolation = cv2.INTER_AREA)
                print "category %d curent %d total %d"%(i,sd,len(elem.keys()))             
                rs=random.random()
                if rs<p_train:
                    if not 'X_train' in locals():
                        X_train=im[None,...]
                    else:
                      X_train=np.concatenate((X_train,im[None,...]), axis=0)      
                    if not 'targets_train' in locals():
                      targets_train=np.array([i])
                    else:
                      targets_train=np.concatenate((targets_train,np.array([i])))
               
                elif p_train<=rs<(p_val+p_train):
                    if not 'X_val' in locals():
                        X_val=im[None,...]
                    else:
                        X_val=np.concatenate((X_val,im[None,...]), axis=0)      
                    if not 'targets_val' in locals():
                        targets_val=np.array([i])
                    else:
                        targets_val=np.concatenate((targets_val,np.array([i])))
               
                else:
                    if not 'X_test' in locals():
                        X_test=im[None,...]
                    else:
                        X_test=np.concatenate((X_test,im[None,...]), axis=0)      
                    if not 'targets_test' in locals():
                        targets_test=np.array([i])
                    else:
                        targets_test=np.concatenate((targets_test,np.array([i])))
                sd+=1

            # print elem
        # for image,category in bigdataset[key]:
        #     print image,category
    
            if not 'targets_train' in locals():
                X_test=np.array(0,ndmin=3)
                targets_train=np.array(0)
            if not 'targets_val' in locals():
                X_val=np.array(0,ndmin=3)                
                targets_val=np.array(0)
            if not 'targets_test' in locals():
                X_test=np.array(0,ndmin=3)  
                targets_test=np.array(0)                
           
            #typecast targets
            targets_test=targets_test.astype(np.int32)
            targets_val=targets_val.astype(np.int32)
            targets_train=targets_train.astype(np.int32)


            # apply some very simple normalization to the data
            X_test=X_test.astype(np.float32)
            X_val=X_val.astype(np.float32)
            X_train=X_train.astype(np.float32)

            X_test -= X_test.mean()
            X_test /= X_test.std()

            X_val -= X_val.mean()
            X_val /= X_val.std()    

            X_train -= X_train.mean()
            X_train /= X_train.std()

            batch={'X_train':X_train,'targets_train':targets_train,'X_val':X_val,'targets_val':targets_val,'X_test':X_test,'targets_test':targets_test}
            pkl=open(key+'.pkl','wb')
            pickle.dump(batch,pkl,pickle.HIGHEST_PROTOCOL)
            pkl.close()

            del targets_test
            del targets_val
            del targets_test
            del X_test
            del X_val
            del X_train        



load_Imagedata('frames')
