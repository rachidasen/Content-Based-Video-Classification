import cv2
import sys
import os
 
# list of all classes
 
classes=('basketball','diving','horse_riding','soccer_juggling','swing','trampoline_jumping','walking','biking',
         'golf_swing','tennis_swing','volleyball_spiking');
# get the parent directory where this program is stored
dir=os.getcwd()
print dir
# concatenate the path to videos' folder
save=os.path.join(dir,"frames")
dir=os.path.join(dir,"frames")
if not os.path.exists(save):
     os.mkdir(save)
# for type in classes:
category='basketball'
rootdir=os.path.join(dir,category)
print rootdir
 
#     print subFolders,files
print "Name of video file"
for dirpath,dirname,files in os.walk(rootdir):
    print "dirname",type(dirpath)
    x=dirpath.rfind("/")
    print dirpath[x+1:]
    
    if not os.path.exists(os.path.join(save,dirpath[x+1:],dirpath)):
        os.mkdir(os.path.join(save,dirpath[x+1:],dirpath))
    files=glob.glob("*.mpg")
    if files:
        print 'h'
        for vid in files:
#           capturing the location of video
            print dirpath
            video_dir=os.path.join(dirpath,vid)
            video = cv2.VideoCapture(os.path.join(dirpath,vid))
            i=1
            ret=True
            while(True):
                ret,frame=video.read()
                
            # making frames of a video
#             if video.grab()