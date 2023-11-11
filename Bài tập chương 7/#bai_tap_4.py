# Nhập 3 số từ bàn phím
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

# Tìm số lớn nhất trong 3 số
max = a # Giả sử a là số lớn nhất
if b > max: # Nếu b lớn hơn max
    max = b # Gán max bằng b
if c > max: # Nếu c lớn hơn max
    max = c # Gán max bằng c

# In ra số lớn nhất trong 3 số
print("Số lớn nhất trong 3 số là", max)