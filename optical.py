import cv2
import sys
import os
import glob
import numpy as np
# list of all classes
def gen_frame(path): 
    classes=('basketball','diving','horse_riding','soccer_juggling','swing','trampoline_jumping','walking','biking',
             'golf_swing','tennis_swing','volleyball_spiking');
    # get the parent directory where this program is stored
    dir=path
    #print dir
    # concatenate the path to videos' folder
    save=os.path.join(dir,"frames")
    dir=os.path.join(dir,"frames")
    count=0
    #print dir
    #print save
    if not os.path.exists(save):
         os.mkdir(save)
    for category in classes:
        #print category
    # category='basketball'
        rootdir=os.path.join(dir,category)
        #print rootdir
         
        #     print subFolders,files
        print "Name of video file"
        
        #count+=1
        #count2=0
        for dirpath,dirname,files in os.walk(rootdir):
            # print "dirname",type(dirpath)
            #print files
            """x=dirpath.rfind("/")
            print x
            print dirpath[x+1:],dirpath
            print "files",files"""
            #print dirpath
            # if not os.path.exists(os.path.join(save,dirpath[x+1:],dirpath)):
            #     os.mkdir(os.path.join(save,dirpath[x+1:],dirpath))
            files=glob.glob(dirpath+"/*.mpg")
            #print files

            #print "\n"
            #print count2
            #count2+=1
            #print "/n"
            if files:
                print files
                #print count
                #count+=1
                for video_dir in files:
        #           capturing the location of video
                    print "dirpath",dirpath,"video",video_dir
                    print count
                    count+=1
                    # video_dir=os.path.join(dirpath,vid)
                    # print video_dir
                    x=video_dir.rfind(".")
                    new=video_dir[:x]   
                    if not os.path.isdir(new):
                        os.mkdir(new)
                        # os.system("mkdir new/optical_flow_images")


                    count=0

                    video = cv2.VideoCapture(video_dir)
                    if video.grab():
                        
                        # Now write your code
                        # input availabe
                        #   video =name of video
                        #  directory= new
                        try:
                            
                            ret, frame1 = video.read()
                            frame1=cv2.resize(frame1,(150,150))
                            prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

                            while(1):
                                ret, frame2 = video.read()

                                if frame2==None:
                                    break
                                count+=1
                                if count==300:
                                    break
                                #print ()

                                frame2=cv2.resize(frame2,(150,150))
                                next=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

                                flow=cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

                                horz = cv2.normalize(flow[...,0], None, 0, 255, cv2.NORM_MINMAX)
                                vert = cv2.normalize(flow[...,1], None, 0, 255, cv2.NORM_MINMAX)
                                horz = horz.astype('uint8')
                                vert = vert.astype('uint8')
                                pic=new+'/h'+str(count)
                                pic1=new+'/v'+str(count)

                                cv2.imwrite(pic+'.jpg',horz)
                                cv2.imwrite(pic1+'.jpg',vert)

                                prvs = next

                            video.release()
                        except Exception, e:
                            print e
                        # generate optical frames and write to the directory new
                        
                        #cv2.destroyAllWindows()






                        # print "generating frames"
                        # i=0
                        # #ret=True
                        # ret,frame1=video.read()
                        # print ret
                        # if frame1==None:
                        #     break
                        # while(ret):
                        #     try:
                        #         #ret,frame1=video.read()
                        #         #print ret
                        #         #print frame1
                        #         if ret:
                        #             frame1=cv2.resize(frame1,(150,150))
                        #             prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
                        #             #hsv = np.zeros_like(frame1)
                        #             #hsv[...,1] = 255

                                    
                        #             ret, frame2 = video.read()
                        #                 next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

                        #                 flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

                        #                 mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
                        #                 hsv[...,0] = ang*180/np.pi/2
                        #                 hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
                        #                 bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

                        #                 #cv2.imshow('frame2',bgr)
                        #                 #k = cv2.waitKey(300) & 0xff
                        #                 print "here k"
                        #                 if k == 27:
                        #                     print "here 2",k
                        #                     break
                        #                 #elif k == ord('s'):
                        #                 pic=new+"/"+'opticalfb'+str(i)+".jpg"
                        #                 pic1=new+"/"+'opticalhsv'+str(i)+".jpg"
                        #                 print pic
                        #                 print pic1
                        #                 cv2.imwrite(pic,frame2)
                        #                 cv2.imwrite(pic1,bgr)
                        #                 i+=1
                        #                 prvs = next
                        #             #pic=new+"/"+str(i)+".bmp"
                        #             # print pic
                        #             #cv2.imwrite(pic,frame)
                        #             print "outside loop"
                        #             #i+=1"""
                        #     except (IOError,RuntimeError, TypeError, NameError):
                        #         print "skipping"
                    # os.remove(video_dir)
                    # print i
                    # making frames of a video
    #             if video.grab()"""

if __name__=="__main__":
    # edit this path where the video is present
    gen_frame("/home/karpathy")
