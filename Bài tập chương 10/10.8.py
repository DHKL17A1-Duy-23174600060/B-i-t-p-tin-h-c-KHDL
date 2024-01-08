import datetime
day = int(input("Nhập ngày:"))
month = int(input("Nhập tháng:"))
year = int(input("Nhập năm:"))

date = datetime.datetime(year,month,day)
formatted_date= date.strftime("%d - %m - %y")
print("Ngày tháng năm vừa nhập vào",formatted_date)

is_leap_year=date.year%4==0 and (date.year % 100!= 0 or date.yaer % 400 ==0)
if is_leap_year:
    print(date.year,"là năm nhuận")
else:
    print(date.year,"không là năm nhuận")

weekday = date.strftime("%A")
print("Ngày/Tháng/Năm nhập vào là",weekday)

num_days=(date.replace(day=1)+datetime.timedelta(days=32)).replace(day=1)-datetime.timedelta(days=1)
print("Tháng",date.strftime("%B"),"có",num_days.day,"ngày")
