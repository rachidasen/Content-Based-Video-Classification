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
USING VGG_NET
-----------

   


