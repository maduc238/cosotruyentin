import numpy as np
#hàm toán tử XOR từ hai bit x y (x dài hơn y)
def xor(x,y,key):
    result = []
    for i in range (key, len(y)):
        if x[i] == y[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)  #lưu thành 1 mảng

#hàm phép chia lấy dư
def sodu(sobichia, sochia):
    """
    Hàm lấy số dư của một phép chia
    """
    #biến i là con trỏ chạy quan trọng trong hàm của phép chia này
    #gán giá trị ban đầu của i là chiều dài bit của số chia
    i = len(sochia)

    #từ chiều dài của số chia có được, lấy 'i' bit của số bị chia để thực hiện phép xor
    #gọi phần từ nhỏ lấy được của số bị chia là chia_process
    chia_process = sobichia[0 : i]

    #dùng vòng lặp bắt đầu chia
    while i < len(sobichia):
        #nếu số bit đầu tiên của chia_process là 1, thực hiện phép xor bình thường của sochia và chia_process
        if chia_process[0] == '1':
            #thu được mảng mới, đồng thời dịch mảng sang trái, nối thêm bit thứ i của số bị chia (như phép dịch dần của phép chia), không làm thay đổi kích thước của mảng chia_process
            chia_process = xor(sochia, chia_process, 1) + sobichia[i]
        #ngược lại, nếu số bit đầu tiên là 0 thì thực hiện tương tự, tuy nhiên chỉ cần thay chia process bằng các bit 000... để giữ nguyên giá trị
        else:
            #sobichia lúc này là 000... (i phần tử số 0)
            chia_process = xor('0'*i, chia_process, 1) + sobichia[i]
        #tăng thêm vị trí của con trỏ i trong số bị chia
        i += 1
 
    #đến lúc này tràn hết giá trị i, làm các tương tự với chia_process cuối cùng của phép chia
    if chia_process[0] == '1':
        chia_process = xor(sochia, chia_process, 1)
    else:
        chia_process = xor('0'*i, chia_process, 1)

    #cuối cùng thu được mảng chứa các bit dư của phép chia này
    so_du = chia_process
    return so_du

#Hàm mã hóa dữ liệu gửi
def mahoa(data, key):
    #với data là Q(x), key là G(x)
    key_length = len(key)
    #thêm các bit 0000... (với chiều dài của key - 1)
    appended_data = data + '0'*(key_length-1)
    #lấy số dư của nó với key
    du = sodu(appended_data, key)
    #sau khi lấy được số dư, thêm số dư đằng sau dữ liệu: là P(x)
    mahoa = data + du
    return mahoa

def dao(a):
    result = []
    for i in range(0,len(a)):
        result.append(a[len(a)-i-1])
    return ''.join(result)

#hàm nhân 2 bin với nhau
def nhan(tich1, tich2):
    t1 = dao(tich1)
    t2 = dao(tich2)
    temp = "0"*(len(t1)-1)
    for i in range (0,len(t2)):
        temp = temp + "0"
        if t2[i] == '1':
            temp = xor(temp,i*"0"+t1,0)
        else:
            temp = xor(temp,"0"*(len(t1)+i),0)
    return dao(temp)

def Wi(Px,Gx):
    Rx = sodu(Px,Gx)
    count = 0
    for i in Rx:
        if i == '1': count += 1
    return count

#hàm dịch trái và dịch phải
def dichtrai(a):
    result = a[1:]
    return result + a[0]
def dichphai(a):
    result = a[:-1]
    return a[-1] + result

#hàm hiện kết quả thương của phép chia 2 mã với nhau
def thuong(sobichia, sochia):
    """
    Hàm tính thương của một phép chia bit
    """
    i = len(sochia)
    chia_process = sobichia[0 : i]
    result = []
    #thuật toán giống như lấy số dư
    while i < len(sobichia):
        if chia_process[0] == '1':
            chia_process = xor(sochia, chia_process, 1) + sobichia[i]
            result += "1"
        else:
            chia_process = xor('0'*i, chia_process, 1) + sobichia[i]
            result += "0"
        i += 1
    if chia_process[0] == '1':
        chia_process = xor(sochia, chia_process, 1)
        result += "1"
    else:
        chia_process = xor('0'*i, chia_process, 1)
        result += "0"
    return ''.join(result)

def check1(n,k):
    if 2**k > (2**n)/(1+n):
        print("Không thể tạo được từ mã check lỗi")
        return False
    elif n > 21:
        print("n vượt quá giới hạn cho phép")
        return False
    else: return True

def Xor(a,b):
    result = 0
    if a != b: result = 1
    return result

def SquareMatrix(input, shape):
    """
    Tạo ma trận vuông từ một chuỗi
    """
    X = []
    for i in range(len(input)):
        X.append(int(input[i]))
    _X = np.array(X)
    _X = np.reshape(_X, (shape, shape))
    return _X

def Dot(A, B):
    result = 0
    for i in range(len(A)):
        result = Xor(result, A[i]*B[i])
    return result

def DotBin(A, B):
    """
    Nhân hai ma trận A B với nhau theo bin
    """
    result = np.zeros((len(A),len(B[0,:])),dtype=int)
    for i in range(len(A)):
        for j in range(len(B[0,:])):
            result[i,j] = Dot(A[i],B[:,j])
    return result