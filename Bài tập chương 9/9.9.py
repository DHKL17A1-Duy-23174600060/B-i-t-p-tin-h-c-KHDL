def kiem_tra_so_hoan_hao(num):
    x = 0
    for i in range(1,num):
        if num % i ==0:
            x +=i
    if x == num:
        return True
    else:
        return False
    
print(kiem_tra_so_hoan_hao(28))
