# 9.4: xây dựng phương thức 
import math
n= int(input("Nhập giá trị n:"))
x =int(input("Nhập giá trị x:"))
def tinh_S(n,x):
    S=(x**2+1)**n
    return S
S = (x**2+1)**n
print("Giá trị S là:",S)