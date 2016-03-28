from PIL import Image
import cPickle as pickle
import numpy as np
import os
import cv2
import glob
def convert():
	classes=('basketball','diving','horse_riding','soccer_juggling','swing','trampoline_jumping','walking','biking',
         'golf_swing','tennis_swing','volleyball_spiking');

	path=os.getcwd()
	path=os.path.join(path,'frames')
	
	dataset=np.zeros((200,200,3))
	label=[]
	print path
	folders=os.listdir(path)
	# for i,category in enumerate(classes):
	category='basketball'
	label.append(category)
	if os.path.isdir(path+"/"+category):
		rootdir=os.path.join(path,category)
		print rootdir
		files=glob.glob(rootdir+"/**/**/*.jpg")
		for file in files:
			print file
			a=cv2.imread(file)
			# dim=(200,200)
			a=cv2.resize(a,(200,200),interpolation = cv2.INTER_AREA)
			# print "a",a
			# print "a.shape",a.shape
			dataset=np.vstack((dataset,a))
		# print files
	dataset=np.asarray(dataset)
	label=np.asarray(label)
	print label.shape
	print "dataset",dataset.shape
	return dataset
	print dataset

			# for dirpath,dirname,files in os.walk(rootdir):
			# 	# print dirname,files
			# 	print files		
				# cv2.imread()		



# 	dataset=[]
# 	labels=[]
# 	#return 
# 	label_id=0
# 	for folder in l1:
# 		print folder,label_id
# 		if os.path.isdir(pathmen+"/"+folder):	
# 			#print len(os.listdir(pathmen+"/"+folder))
# 			img_names=os.listdir(pathmen+"/"+folder)
# 			#print img_names[:5]
# 			count=0
# 			sk=0
# 			for fn in img_names:
# 				#print fn
# 				try:
# 					shoe_image = Image.open(pathmen+"/"+folder+"/"+fn)				
# 					shoe_image=shoe_image.resize((32,32),Image.ANTIALIAS)
# 					shoe_image=np.array(shoe_image,dtype="f")
# 					if shoe_image.shape != (32,32,3):
# 						print shoe_image.shape
# 						continue
# 					dataset.append(shoe_image)
# 					labels.append(label_id)
# 					count+=1
# 					if count>=2500:
# 						break
# 				except:
# 					print fn + "skipped...\n"
# 					sk+=1	
		
# 			print sk
# 			label_id+=1


# 	pathwomen=os.path.join(path,"womens")
# 	for folder in l2:
# 		print folder,label_id
# 		if os.path.isdir(pathwomen+"/"+folder):	
# 			#print len(os.listdir(path+"/"+folder))
# 			img_names=os.listdir(pathwomen+"/"+folder)
# 			#print img_names[:5]
# 			count=0
# 			sk=0

# 			for fn in img_names:
# 				#print fn
# 				try:
# 					shoe_image = Image.open(pathwomen+"/"+folder+"/"+fn)				
# 					shoe_image=shoe_image.resize((32,32),Image.ANTIALIAS)
# 					shoe_image=np.array(shoe_image,dtype="f")
# 					if shoe_image.shape != (32,32,3):
# 						print shoe_image.shape
# 						continue
# 					dataset.append(shoe_image)
# 					labels.append(label_id)
# 					count+=1
# 					if count>=2500:
# 						break
# 				except:
# 					print fn + "skipped...\n"
# 					sk+=1	
		
# 			print sk
# 			label_id+=1

# 	print len(dataset),len(labels)		

# 	data=dataset,labels

# 	pkl=open("shoes_dataset32.pickle","wb")
# 	pickle.dump(data,pkl,pickle.HIGHEST_PROTOCOL)#for binary file protocol>=1
# 	pkl.close()











convert()	