# 9.5
import math
n= int(input("Nhập giá trị n:"))
x= int(input("Nhập giá trị x:"))
def tinh_A(n,x):
    A= ((x**2+x+1)**n)+(x**2-x+1)**n
    return A
A=((x**2+x+1)**n)+(x**2-x+1)**n
print("Giá trị A=",A)
