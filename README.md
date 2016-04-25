# major
**PREREQUISITES
sudo apt-get install python-software-properties #to install "add-apt-repository"
$ sudo add-apt-repository ppa:biometrics/bob #only the first time
$ sudo apt-get update #repeat this every time you need to update
$ sudo apt-get install bob

******************************************************
      SAVING NUMPY ARRAY TO HDF

*****************************************************

import tables
h5file = tables.openFile('test.h5', mode='w', title="Test Array")
root = h5file.root
h5file.createArray(root, "test", a)
h5file.close()
A = numpy.array(range(4), 'int8').reshape(2,2)
>>> f = bob.io.base.HDF5File('testfile1.hdf5', 'a')
>>> f.set('my_array', A)
>>> del f



*********************************************
        LOADING HDF BACK TO NUMPY

*********************************************

f = bob.io.base.HDF5File('testfile1.hdf5') #read only
>>> f.read('my_integer') #reads integer
5
>>> print(f.read('my_array')) # reads the array
[[0 1]
 [2 3]]
>>> del f

*********************************************
            DATASET DETAILS
**********************************************
********SPATIAL (SPLIT INTO 19 DATASETS) 
>>Total no.of (training) frames (size[150,150])= 243561
>>Total no.of (validation) frames            = 15217
>>Total no.of (testing                       = 45664 


*****SPATIAL IMAGE **********************
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
USING ALEX_NET (partially)
-----------
*********************************
  		ABOUT THE NETWORK
**********************************

>>Input_Layer	batch size x color channels x image dimension 1 x image dimension 2

>>Conv2DLayer: The most important keywords are _numfilters and _filtersize. The former indicates the number of channels -- the more you choose, the more different filters can be learned by the CNN. Generally, the first convolutional layers will learn simple features, such as edges, while deeper layers can learn more abstract features. Therefore, you should increase the number of filters the deeper you go. The _filtersize is the size of the filter/kernel. The current consensus is to always use 3x3 filters, as these allow to cover the same number of image pixels with fewer parameters than larger filters do.

>>MaxPool2DLayer: This layer performs max pooling and hopefully provides translation invariance. We need to indicate the region over which it pools, with 2x2 being the default of most users.

>>DenseLayer: This is your vanilla fully-connected layer; you should indicate the number of 'neurons' with the _numunits argument. The very last layer is assumed to be the output layer. We thus set the number of units to be the number of classes, 10, and choose softmax as the output nonlinearity, as we are dealing with a classification task.

>>DropoutLayer: Dropout is a common technique to regularize neural networks. It is almost always a good idea to include dropout between your dense layers.

   


