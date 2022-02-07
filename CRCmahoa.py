from library import *

while 1:
    n = int(input("Nhập chiều dài mã mang tin n: "))
    k = int(input("Nhập chiều dài từ mã chứa thông tin k: "))
    c = check1(n,k)
    if c == True: break

while 1:
    Qx = input("Nhập đa thức chứa thông tin Qx: ")
    count = 0
    if len(Qx) != k:
        print("Nhập Qx không đúng chiều dài là k =",k)
        count += 1
    for i in Qx:
        if i != '0' and i != '1': count += 1
    if count == 0: break
    else: print("Đầu vào không hợp lệ")

check1(n,len(Qx))

if n == 3: Gx = "111"
elif n == 4: Gx = "11"
elif n == 5: Gx = "11111"
elif n == 6: Gx = "111"
elif n == 7: Gx = "1011"
elif n == 8: Gx = "11"
elif n == 9: Gx = "1001001"
elif n == 10: Gx = "11111"
elif n == 11: Gx = 11*"1"
elif n == 12: Gx = "10101"
elif n == 13: Gx = 13*"1"
elif n == 14: Gx = "1011"
elif n == 15: Gx = "11001"
elif n == 16: Gx = "11"
elif n == 17: Gx = 17*"1"
elif n == 18: Gx = "1001001"
elif n == 19: Gx = 19*"1"
elif n == 20: Gx = "11111"
elif n == 21: Gx = "1110101"

if len(Gx) > (n - len(Qx) + 1):
    print("Không thể mã hóa được")
    exit(0)
else:
    Gx = "0"*(n - len(Qx) + 1 - len(Gx)) + Gx

Rx = sodu(Qx + (n-len(Qx))*"0",Gx)
if(len(Rx) < (n-len(Qx))):
    Rx = (n-len(Qx)-len(Rx))*"0" + Rx

print("Đa thức sinh được sử dụng Gx:",Gx)
print("Px (mã tin không hệ thống):",nhan(Qx,Gx))
print("Px (mã tin hệ thống):      ",Qx+Rx)