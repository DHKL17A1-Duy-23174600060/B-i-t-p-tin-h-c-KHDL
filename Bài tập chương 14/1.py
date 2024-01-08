# xử lý ngoại lệ
def xu_ly_ngoai_le(a,b,c):
    return a+b>c and b+c>a and c+a>b


try:
    a=float(input("Nhập đọ dài cạnh a:"))
    b=float(input("nhập độ dài cạnh b:"))
    c=float(input("Nhập độ dài cạnh c:"))

    if a<=0 or b<=0 or c<=0 or not xu_ly_ngoai_le(a,b,c):
        raise ValueError("Không tồn tại tam giác với các giá trị nhập vào.")
    
    print("Ba cạnh a,b,c là 3 cạnh của một tam giác")
except ValueError as ve:
    print(f"Lỗi :{ve}. Hãy nhập lại các giá trị là số dương và thỏa mãn điều kiện tồn tại tam giác")
except Exception as e:
    print(f"Lỗi không xác định :{e}.")

