# -*- coding: utf-8 -*-

import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 1]])
print(a.shape)

# Get a specific element [R , C]
print(a[1, 2])  # 8

# Get a specific element [R, :]
print(a[0, :])

# Get a specific column [: , C]
print(a[:, 2])

#
a[1,2] = 20
print(a)

#3-D example
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#Get specific element (Work outside in)
print(b[0,0,1])

#Example:
    
ab = np.array([[[1,2,3,4,5] , [6,7,8,9,10]] , [[11,12,13,14,15] , [16,17,18,19,20]]])

print(ab)
print(ab[ 1 , 0 , 2])
print(ab[: , 0 , 1])

