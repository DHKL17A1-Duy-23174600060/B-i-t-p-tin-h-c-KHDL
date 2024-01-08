# 11.5
my_list=['1','-3','-4','5','8']
num_elements=int(input("Nhập số phần tử trong list:"))

for i in range(num_elements):
    element=int(input("Nhập phần tử thứ {}:".format(i+1)))
    my_list.append(element)

prime_numbers=[num for num in my_list if num >1 and all(num % i!=0 for i in range(2,int(num**0.5)+1))]
print("các số nguyên tố trong list :{}".format(prime_numbers))

positive_numbers=[num for num in my_list if num>0]
negative_numbers=[num for num in my_list if num <0]

if positive_numbers:
    avg_positive=sum(positive_numbers)/len(positive_numbers)
    print("trung bình cộng các phần tử dương:{}".format(avg_positive))
else:
    print("Không có phần tử âm trong list.")

max_value=max(my_list)
min_value=min(my_list)
print("giá trị lớn nhất trong list:{}".format(max_value))
print("giá trị nhỏ nhất trong list:{}".format(min_value))
