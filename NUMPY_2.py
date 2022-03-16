# -*- coding: utf-8 -*-

import numpy as np

ab = np.array([[[1,2,3,4,5] , [6,7,8,9,10]] , [[11,12,13,14,15] , [16,17,18,19,20]]])

#All 0s matrix:
print(np.zeros((2,10))) , print("**")

#All 1s matrix:
print(np.ones((2,10) , dtype = 'int32'  )) , print("**")

#Any other numbers:
print(np.full((2,2,2) , 10))

#Any other numbers (full_like)  to take a shape already that i have:
print(np.full_like(ab , 4))

#Random numbers:
print(np.random.randint(1 , 10 , size = (1,10) ))

#The identity matris:
print(np.identity(4))

#Repeat an array:
arr = np.array([[1,2,3] , [4,5,6]])
r1 = np.repeat(arr , 2 , axis = 1)
print(r1)

#Copy:
b = ab.copy()
b[0,0,0] = 90
print(b) #[90]
print("**")
print(ab) #[1]

#35:48