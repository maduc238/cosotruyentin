import numpy as np
from library import *

#ma trận sinh
G = np.array([[1,0,0,0,1,1,0],
            [0,1,0,0,1,0,1],
            [0,0,1,0,0,1,1],
            [0,0,0,1,1,1,1]])
#tin tổ hợp
u = np.array([[1,1,1,0]])
shape = len(G)
A = G[:,:shape]
I = np.eye(shape,dtype=int)

for i in range(1,2**(shape**2)):
    temp = bin(i)[2:].zfill(shape**2)
    if (DotBin(SquareMatrix(temp, shape),A) == I).all(): break

print("Ma trận G ban đầu")
print(G)
print("Cách cộng ma trận")
print(SquareMatrix(temp, shape))
print("Ma trận G sau chuẩn hóa")
G_new = DotBin(SquareMatrix(temp, shape),G)
print(G_new)
H = np.concatenate((G_new[:,shape:].T, np.eye(len(G_new[0,:]) - shape, dtype=int)),axis=1) 
print("Ma trận H")
print(H)
print("Mã tin c thu được")
print(DotBin(u,G_new))