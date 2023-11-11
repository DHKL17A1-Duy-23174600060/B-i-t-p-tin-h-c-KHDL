## Nhập một số từ bàn phím
n = int(input("Nhập một số: "))

# Kiểm tra nếu số đó là số dương
if n > 0:
    # In ra bình thường của số đó
    print("Bình thường của", n, "là", n ** 0.5)
else:
    # In ra thông báo lỗi
    print("Số nhập vào không phải là số dương")