import numpy as np

#Reorganizing Arrays
a = np.array([ [1,2,3,4,5] , [6,7,8,9,10] ])
print(a.shape) # 2,5
print(a.reshape(10,1)) 
print(a.reshape(5,2))

#Load data from file
a = np.genfromtxt('data.txt' , delimiter=',' , dtype='int32')
print(a)

#linspace:
b = np.linspace(1,100,15, dtype="int32")
print(b) #numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

