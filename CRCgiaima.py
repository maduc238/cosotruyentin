from library import *

while 1:
    count2 = 0
    while 1:
        Px = input("Nhập từ mã mang tin Px: ")
        count = 0
        for i in Px:
            if i != '0' and i != '1': count += 1
        if count == 0: break
        else: print("Đầu vào Px không hợp lệ")

    while 1:
        Gx = input("Nhập đa thức sinh Gx: ")
        count = 0
        for i in Px:
            if i != '0' and i != '1': count += 1
        if count == 0: break
        else: print("Đầu vào Gx không hợp lệ")
    if len(Px) <= len(Gx):
        count2 += 1
        print("Không thể thực hiện giải mã, mời thực hiện lại")
    if count2 == 0: break

s = int(input("Nhập số lỗi sai s: "))

#thực hiện giải mã
Gxa = int(Gx)
Gxa = str(Gxa)
i = 0
length = len(Px)
while i < length:
    check = False
    if Wi(Px,Gxa) <= s:
        check = True
        break
    else:
        Px = dichtrai(Px)
    i += 1

if check == True:
    print("Mã hóa được")
    #tính Pdx
    Pdx = dao(xor(dao(Px),dao("0"*(len(Px)-len(Gx)+1) + sodu(Px,Gxa)),0))
    print("Dịch trái:",i,"bit")
    j = 0
    while j < i:
        Pdx = dichphai(Pdx)
        j += 1
    #với mã hệ thống: Qx là k bit đầu tiên của Pdx
    print("Qx (mã tin không hệ thống):",thuong(Pdx,Gxa))
    print("Qx (mã tin hệ thống):      ",Pdx[:len(Px)-len(Gx)+1])
else:
    print("Không mã hóa được")