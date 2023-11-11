# Bài 2: Tính số ngày của một tháng một năm nào đó
# Nhập tháng và năm từ bàn phím
month = int(input("Nhập tháng (1-12): "))
year = int(input("Nhập năm: "))

# Kiểm tra nếu tháng hợp lệ
if 1 <= month <= 12:
    # Khởi tạo biến days để lưu số ngày của tháng
    days = 0

    # Xét các trường hợp cho từng tháng
    if month == 2:
        # Nếu là tháng 2, kiểm tra năm nhuận hay không
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            # Năm nhuận, tháng 2 có 29 ngày
            days = 29
        else:
            # Năm không nhuận, tháng 2 có 28 ngày
            days = 28
    elif month in [4, 6, 9, 11]:
        # Nếu là các tháng có 30 ngày
        days = 30
    else:
        # Nếu là các tháng có 31 ngày
        days = 31

    # In ra kết quả
    print("Tháng", month, "năm", year, "có", days, "ngày")
else:
    # Nếu tháng không hợp lệ, in ra thông báo lỗi
    print("Tháng không hợp lệ")