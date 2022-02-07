import numpy as np
from library import *

A = np.array([[1,0,1,1,1,0,0],
            [1,1,1,0,0,1,0],
            [1,0,0,1,0,1,1]])
B = np.array([[1,0,0,0,1,1,0],
            [0,1,0,0,1,0,1],
            [1,0,1,0,0,1,1],
            [0,1,0,1,1,1,1]])
"""
Lưu ý: Hai ma trận phải nhân được với nhau
Với ma trận 1 hàng, phải để hai ngoặc [[ để tránh việc thành vector
"""
print("Kết quả nhân A với B(T):")
#Muốn thành ma trận chuyển vị chỉ cần thêm .T
print(DotBin(A,B.T))