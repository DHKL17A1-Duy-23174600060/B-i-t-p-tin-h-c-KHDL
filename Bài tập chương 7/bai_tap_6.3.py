# Bài 3: Giải thuật tìm ước số chung lớn nhất của hai số nguyên dương a và b
# Nhập hai số nguyên dương a và b từ bàn phím
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

# Kiểm tra nếu a và b là số nguyên dương
if a > 0 and b > 0:
    # Sử dụng giải thuật Euclid để tìm ước số chung lớn nhất (USCLN)
    def USCLN(a, b):
        if b == 0:
            return a
        return USCLN(b, a % b)

    # Gọi hàm USCLN và in ra kết quả
    print("Ước số chung lớn nhất của", a, "và", b, "là", USCLN(a, b))
else:
    # Nếu a hoặc b không phải là số nguyên dương, in ra thông báo lỗi
    print("Số nhập vào không phải là số nguyên dương")