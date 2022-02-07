import numpy as np
from library import *
from os import system
system("cls")

input = '10101'
output = []

A = np.array([[0,0,0]])
g1 = np.array([[1,0,1]])
g2 = np.array([[0,1,1]])
g3 = np.array([[1,1,1]])

for i in range(len(input)):
    for j in range(1,len(A[0])):
        A[0,len(A[0])-j] = A[0,len(A[0])-j-1]
    A[0,0] = int(input[i])
    output.append(str(DotBin(A,g1.T)[0][0]) + str(DotBin(A,g2.T)[0][0]) + str(DotBin(A,g3.T)[0][0]))

print(output)