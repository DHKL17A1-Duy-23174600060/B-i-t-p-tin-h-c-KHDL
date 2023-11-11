# Nhập một số nguyên N từ bàn phím
N = int(input("Nhập một số nguyên N: "))

# Khởi tạo biến sum để lưu tổng các chữ số của N
sum = 0

# Lặp qua từng chữ số của N
while N > 0:
    # Lấy chữ số cuối cùng của N và cộng vào sum
    sum += N % 10

    # Loại bỏ chữ số cuối cùng của N
    N //= 10

# In ra kết quả
print("Tổng các chữ số của N là", sum)
