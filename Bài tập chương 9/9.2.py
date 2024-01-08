# 9.2
def tinh_can(nam):
    can=["Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"]
    return can[nam % 10]
def tinh_chi(nam):
    chi=["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]
    return chi[nam % 12]

nam_duong_lich=2017
can=tinh_can(nam_duong_lich)
chi=tinh_chi(nam_duong_lich)

print("Năm",nam_duong_lich,"lịch ân là năm",can,chi)