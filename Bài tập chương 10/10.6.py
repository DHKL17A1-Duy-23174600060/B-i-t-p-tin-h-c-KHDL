import math
a = int(input("Nhập giá trị a="))
b = int(input("Nhập giá trị b="))
c = int(input("Nhập giá trị c="))
if a==0:
    print("Phương trình không phải phương trình bậc 2")
else:
    delta = b**2-4*a*c
    if delta<0:
        print("Phương trình vô nghiệm")
    elif delta==0:
        x=-b/2*a
        print("Phương trình có nghiệm kép",x)
    else:
        x1= (-b+math.sqrt(delta)/2*a)
        x2= (-b-math.sqrt(delta)/2*a)
        print("Phương trình có nghiệm x1 =",x1)
        print("Phương trình có nghiệm x2 =",x2)