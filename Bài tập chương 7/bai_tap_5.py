# Nhập 2 số từ bàn phím
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Tìm ước số chung lớn nhất (USCLN) của a và b
def USCLN(a, b):
    if b == 0:
        return a
    return USCLN(b, a % b)

# Tìm bội số chung nhỏ nhất (BCNN) của a và b
def BCNN(a, b):
    return (a * b) / USCLN(a, b)

# In ra kết quả
print("BCNN của", a, "và", b, "là", BCNN(a, b))