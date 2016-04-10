import cPickle as pickle
# import numpy as np
import os
# import sys
import glob
# import cv2
import random

def classify_dataset(imagedir='frames'):
    print("load images")
    classes=('basketball','diving','horse_riding','soccer_juggling','swing','trampoline_jumping','walking','biking',
         'golf_swing','tennis_swing','volleyball_spiking');
# get the parent directory where this program is stored
    total=[]
    trainy=[]
    valy=[]
    testy=[]
    train=[]
    test=[]
    val=[]
    # imagedir=os.path.join(os.getcwd(),imagedir)
    for i,category in enumerate(classes):
        #print "category %d" %i
        path=os.path.join(imagedir,category)
        # print path
        files=glob.glob(path+"/**/**/*.jpg")
        # print files
        length=len(files)
        # print files
        # for i in 
        train.extend(files[:int(0.8*length)])
        val.extend(files[int(0.8*length):int(0.85*length)])
        test.extend(files[int(0.85*length):])
        # total=total+files
        trainy.extend([i]*int(0.8*length))
        valy.extend([i]*int(0.05*length))
        testy.extend([i]*int(0.15*length))
    # print total
    train=zip(train,trainy)
    val=zip(val,valy)
    test=zip(test,testy)
    for i in range(20):
        random.shuffle(train)
        random.shuffle(val)
        random.shuffle(test)

    print "len of train %d"%len(train)
    print "len of test %d"%len(test)
    print "len of val %d"%len(val)

    pkl=open('training.pkl','wb')
    pickle.dump(train,pkl,pickle.HIGHEST_PROTOCOL)
    pkl.close()
    pkl=open('testing.pkl','wb')
    pickle.dump(val,pkl,pickle.HIGHEST_PROTOCOL)
    pkl.close()
    pkl=open('validation.pkl','wb')
    pickle.dump(test,pkl,pickle.HIGHEST_PROTOCOL)
    pkl.close()


if __name__=="__main__":
# run this programme to classify dataset where frames are present
	classify_dataset('frames')
