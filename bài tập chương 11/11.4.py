# 11.4
list_numbers=0

while True:
    value=int(input("Nhập giá trị:"))
    list_numbers.append(value)

    continue_input=int(input("Tiếp tục nhập giá trị?1:Có,0:Không"))
    if continue_input == 0:
        break
x=int(input("Nhập giá trị cần tìm x:"))

print("List:",list_numbers)
print("Tổng các giá trị trong list:",sum(list_numbers))
print(x,"xuất hiện",list_numbers.count(x),"lần trong list")

larger_numbers=[num for num in list_numbers if num>x]
print(x,"Không lớn hơn tất cả các số trong list")
print("các số lớn hơn",x,"trong list",larger_numbers)
