# Nhập một số tự nhiên N từ bàn phím
N = int(input("Nhập một số tự nhiên N: "))

# Kiểm tra nếu N là số tự nhiên
if N > 0:
    # In ra các số nguyên trong phạm vi từ 1 đến N
    print("Các số nguyên trong phạm vi từ 1 đến", N, "là:")
    for i in range(1, N + 1):
        print(i, end=" ")
else:
    # In ra thông báo lỗi
    print("Số nhập vào không phải là số tự nhiên")