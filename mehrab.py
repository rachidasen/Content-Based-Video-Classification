import multiprocessing as mp
import signal
import time
import sys
import os
import copy_reg
import types
import cPickle as pickle
import numpy as np
import os
import sys
import glob
import cv2
import random



# def load_Imagedata(imagedir='frames', minNumSamplesPerClass=100, imsize=(200,200), p_train=0.6, p_val=0.2):
#     print("load images")
#     classes=('basketball','diving','horse_riding','soccer_juggling','swing','trampoline_jumping','walking','biking',
#          'golf_swing','tennis_swing','volleyball_spiking');
# # get the parent directory where this program is stored
#     # batch=4

#     for i,category in enumerate(classes):
#         print "category %d" %i
#         path=os.path.join(imagedir,category)
#         files=glob.glob(path+"/**/**/*.jpg")
        
    #         #load the images one-by-one
    #     print len(files)
    #     # batch=4

    #     # sd=0
    #     for file in files:
    #         # print "file",file
    #         # print "hello"
    #         sd+=1
    #         img=cv2.imread(file)
    #         # print img.shape 
    #         im=cv2.resize(img,imsize,interpolation = cv2.INTER_AREA)
    #         print "category %d curent %d total %d"%(i,sd,len(files))         
    # #         #resize image 
    # #         # print "hello" 
    # #         # print im.shape            
    #         rs=random.random()
    #         if rs<p_train:
    #             if not 'X_train' in locals():
    #                 X_train=im[None,...]
    #             else:
    #               X_train=np.concatenate((X_train,im[None,...]), axis=0)      
    #             if not 'targets_train' in locals():
    #               targets_train=np.array([i])
    #             else:
    #               targets_train=np.concatenate((targets_train,np.array([i])))
           
    #         elif p_train<=rs<(p_val+p_train):
    #             if not 'X_val' in locals():
    #                 X_val=im[None,...]
    #             else:
    #                 X_val=np.concatenate((X_val,im[None,...]), axis=0)      
    #             if not 'targets_val' in locals():
    #                 targets_val=np.array([i])
    #             else:
    #                 targets_val=np.concatenate((targets_val,np.array([i])))
           
    #         else:
    #             if not 'X_test' in locals():
    #                 X_test=im[None,...]
    #             else:
    #                 X_test=np.concatenate((X_test,im[None,...]), axis=0)      
    #             if not 'targets_test' in locals():
    #                 targets_test=np.array([i])
    #             else:
    #                 targets_test=np.concatenate((targets_test,np.array([i])))
       
    # if not 'targets_train' in locals():
    #     X_test=np.array(0,ndmin=3)
    #     targets_train=np.array(0)
    # if not 'targets_val' in locals():
    #     X_val=np.array(0,ndmin=3)                
    #     targets_val=np.array(0)
    # if not 'targets_test' in locals():
    #     X_test=np.array(0,ndmin=3)  
    #     targets_test=np.array(0)                
   
    # #typecast targets
    # targets_test=targets_test.astype(np.int32)
    # targets_val=targets_val.astype(np.int32)
    # targets_train=targets_train.astype(np.int32)


    # apply some very simple normalization to the data
    # X_test=X_test.astype(np.float32)
    # X_val=X_val.astype(np.float32)
    # X_train=X_train.astype(np.float32)

    # X_test -= X_test.mean()
    # X_test /= X_test.std()

    # X_val -= X_val.mean()
    # X_val /= X_val.std()    

    # X_train -= X_train.mean()
    # X_train /= X_train.std()        


    # #permute dimensions.
    # # The data has to have the layer dimension before the (x,y) dimension, as the conv. filters are applied to each layer and expect them to be in that order
    # # The shape convention: (examples, channels, rows, columns)
    # if numChannels==1: #add channel dimension if image is grayscale
    #     X_test = np.expand_dims(X_test, axis=4)
    #     X_val = np.expand_dims(X_val, axis=4)
    #     X_train = np.expand_dims(X_train, axis=4)      

    #     X_test = np.transpose(X_test, (0, 3, 1, 2))
    #     X_val = np.transpose(X_val, (0, 3, 1, 2))
    #     X_train = np.transpose(X_train, (0, 3, 1, 2))

    # dataset={'X_train':X_train,'targets_train':targets_train,'X_val':X_val,'targets_val':targets_val,'X_test':X_test,'targets_test':targets_test} 
    # pkl=open("uc11.pickle","wb")
    # pickle.dump(dataset,pkl,pickle.HIGHEST_PROTOCOL)#for binary file protocol>=1
    # print "success"
    # pkl.close()
    # return X_train, targets_train, X_val, targets_val, X_test, targets_test


 
 
def _pickle_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)
 
copy_reg.pickle(types.MethodType, _pickle_method)
 
 
class Multiprocessing:
    def __init__(self):
        self.pid = {}
        self.classes=('basketball','diving','horse_riding','soccer_juggling','swing','trampoline_jumping','walking','biking',
         'golf_swing','tennis_swing','volleyball_spiking')
 
    def worker(self, file, i,p_train=0.6, p_val=0.2):
        sd=1
        import time
        img=cv2.imread(file)
        print file
        im=cv2.resize(img,(200,200),interpolation = cv2.INTER_AREA)
        # print "category %d curent %d total %d"%(i,sd,len(files))
        # time.sleep(np.random.rand())
        rs=random.random()
        X_train = -1
        X_test = -1
        X_val = -1
        if rs<p_train:
            traningx.append(im[None,...])

            traningy.append([i])
            
       
        elif p_train<=rs<(p_val+p_train):
            validationx.append([im[None,...]])        
            validationy.append([i])

           
       
        else:
            testingx.append([im[None,...]])      
            testingy.append([i])
        # print traningy, validationy, testingy
        # ar.append([])
        # [x, targe], [], []
    def start(self, imagedir='frames'):
        """.."""
        p = mp.Pool(processes=3)
        for i,category in enumerate(self.classes):
            print "category %d" %i
            path=os.path.join(imagedir,category)
            files=glob.glob(path+"/**/**/*.jpg")
            flag = 0
            l = []
            # files = files[:9]
            for file in files:
                if flag == 0:
                    l.append(file)
                    if len(l) == 9:
                        flag = 1
                if flag == 1:
                    plist = []
                    for f in l:
                        plist.append(p.apply_async(self.worker, (f, i)))
                    [j.get() for j in plist]
                    print "done"
                    flag = 0
                    l = []
                    print traningx
                    print traningy
                    print testingy
                    print validationy
            # break
 
if __name__ == '__main__':
    traningx = mp.Manager().list()
    traningy = mp.Manager().list()
    testingx = mp.Manager().list()
    testingy = mp.Manager().list()
    validationx = mp.Manager().list()
    validationy = mp.Manager().list()
    # X_train = mp.Manager().dict()
    # X_test = mp.Manager().dict()
    o = Multiprocessing()
    o.start('frames')
    
    # time.sleep(0.5)
    

