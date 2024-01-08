import math
x = int(input("Nhập giá trị của x="))
n = int(input("Nhập giá trị của n="))
def tinh_A(x,n):
    A=pow((pow(x,2)+x+1),n)+pow((pow(x,2)-x+1),n)
    return A
print("Giá trị A là",tinh_A(x,n))