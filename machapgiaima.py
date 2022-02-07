import numpy as np
from library import *
from os import system
system("cls")

output = ['11','10','00','10','11','01','00','01']
leng = len(output)

g1 = np.array([[1,0,1]])
g2 = np.array([[1,1,1]])
g3 = np.array([[1,1,1]])

def HammingDis(a,b):
    dis = 0
    for itr in range(len(a)):
        if a[itr] != b[itr]: dis += 1
    return dis

Dismin = 100
for i in range(1,2**leng):
    A = np.array([[0,0,0]])
    output_temp = []
    temp = bin(i)[2:].zfill(leng)
    HamDis = 0
    for k in range(leng):
        for j in range(1,len(A[0])):
            A[0,len(A[0])-j] = A[0,len(A[0])-j-1]
        A[0,0] = int(temp[k])
        output_temp.append(str(DotBin(A,g1.T)[0][0]) + str(DotBin(A,g2.T)[0][0]) )
        HamDis += HammingDis(output[k],output_temp[k])
    if HamDis < Dismin: Dismin = HamDis

for i in range(1,2**leng):
    A = np.array([[0,0,0]])
    output_temp = []
    temp = bin(i)[2:].zfill(leng)
    HamDis = 0
    for k in range(leng):
        for j in range(1,len(A[0])):
            A[0,len(A[0])-j] = A[0,len(A[0])-j-1]
        A[0,0] = int(temp[k])
        output_temp.append(str(DotBin(A,g1.T)[0][0]) + str(DotBin(A,g2.T)[0][0]) )
        HamDis += HammingDis(output[k],output_temp[k])
    if Dismin == HamDis:
        print("Input:",temp,". Output:",output_temp,". Hamming distance:",HamDis)
