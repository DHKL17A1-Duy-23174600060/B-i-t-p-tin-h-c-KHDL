# Nhập 2 số tự nhiên m, n (m < n) từ bàn phím
m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n (n > m): "))

# Kiểm tra nếu m, n là số tự nhiên và m < n
if m > 0 and n > 0 and m < n:
    # In ra các số chia hết cho m trong khoảng từ 1 đến n
    print("Các số chia hết cho", m, "trong khoảng từ 1 đến", n, "là:")
    for i in range(1, n + 1):
        if i % m == 0:
            print(i, end=" ")
else:
    # In ra thông báo lỗi
    print("Số nhập vào không hợp lệ")