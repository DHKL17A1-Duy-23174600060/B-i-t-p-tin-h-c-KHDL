# Bài 1: Giải hệ phương trình bậc nhất ax + by = c và dx + ey = f
# Nhập các hệ số a, b, c, d, e, f từ bàn phím
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
d = float(input("Nhập d: "))
e = float(input("Nhập e: "))
f = float(input("Nhập f: "))

# Tính định thức D của hệ số
D = a * e - b * d

# Kiểm tra nếu D khác 0 thì hệ có nghiệm duy nhất
if D != 0:
    # Tính định thức Dx và Dy
    Dx = c * e - b * f
    Dy = a * f - c * d

    # Tính nghiệm x và y
    x = Dx / D
    y = Dy / D

    # In ra kết quả
    print("Hệ phương trình có nghiệm duy nhất:")
    print("x =", x)
    print("y =", y)
else:
    # Kiểm tra nếu D bằng 0 thì hệ có vô số nghiệm hoặc vô nghiệm
    # Tính định thức D1 và D2
    D1 = c * d - a * f
    D2 = b * f - c * e

    # Kiểm tra nếu D1 và D2 cùng bằng 0 thì hệ có vô số nghiệm
    if D1 == 0 and D2 == 0:
        # In ra kết quả
        print("Hệ phương trình có vô số nghiệm")
    else:
        # Ngược lại, hệ vô nghiệm
        # In ra kết quả
        print("Hệ phương trình vô nghiệm")