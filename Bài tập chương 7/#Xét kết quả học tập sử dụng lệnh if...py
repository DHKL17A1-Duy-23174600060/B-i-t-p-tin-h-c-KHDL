#X�t k?t qu? h?c t?p s? d?ng l?nh if...elif...else
diem_TB = eval(input("Nh?p ?i?m trung b�nh: "))
if diem_TB >=0 and diem_TB <=10:
    if diem_TB < 5:
        print("Y?u/K�m!!!")
    elif diem_TB <6:
        print("Trung b�nh!!")
    elif diem_TB <7:
        print("Trung b�nh - Kh�!")
    elif diem_TB <8:
        print("Kh�!!")
    elif diem_TB <9:
        print("Gi?i!!!")
    else:
        print("Xu?t s?c !!!!!")
else:
    print("?i?m nh?p v�o kh�ng x�c ??nh !")