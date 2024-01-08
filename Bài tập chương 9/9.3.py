# 9.3
can_nang=float(input("Nhập số cân nặng(kg):"))
chieu_cao=float(input("Nhập số chiều cao(m):"))
bmi=can_nang/(chieu_cao*chieu_cao)
print("Chỉ số bmi của bạn là:",bmi)
if bmi <18.5:
    print("Bị Gầy")
elif 18.5<= bmi <24.99:
    print("Người bình thường")
else:
    print("Thừa cân")
    