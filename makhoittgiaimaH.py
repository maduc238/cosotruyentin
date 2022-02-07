import numpy as np
from library import *

H = np.array([[1,0,1,1,1,0,0],
            [1,1,1,0,0,1,0],
            [1,0,0,1,0,1,1]])

c = np.array([[1,1,1,0,0,1,0]])

shape = len(H)
A = H[:,shape+1:]
I = np.eye(shape,dtype=int)

for i in range(1,2**(shape**2)):
    temp = bin(i)[2:].zfill(shape**2)
    if (DotBin(SquareMatrix(temp, shape),A) == I).all(): break

print("Ma trận H ban đầu")
print(H)
print("Cách cộng ma trận")
print(SquareMatrix(temp, shape))
print("Ma trận H sau chuẩn hóa")
H_new = DotBin(SquareMatrix(temp, shape),H)
print(H_new)
print("s thu được:")
print(DotBin(c,H_new.T))