Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> height=[74,74,72,72,73,71,76,71]
>>> height_m=[h*0.0254 for h in height]
>>> print("3 chieu cao dau tien:",height_m[:3])
3 chieu cao dau tien: [1.8796, 1.8796, 1.8288]
>>> print("3 chieu cao cuoi cung:",height_m[-3:])
3 chieu cao cuoi cung: [1.8034, 1.9304, 1.8034]
>>> average_heights = sum(height_m)/len(height-m)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    average_heights = sum(height_m)/len(height-m)
NameError: name 'm' is not defined
>>> average_heights=sum(height_m)/len(height_m)
>>> max_heights=max(height_m)
>>> min_heights=min(height_m)
>>> print("cjieu cao trung binh",average_heights)
cjieu cao trung binh 1.8510250000000001
>>> print("chieu cao lon nhat",max_height)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print("chieu cao lon nhat",max_height)
NameError: name 'max_height' is not defined. Did you mean: 'max_heights'?
>>> print("chieu cao lon nhat", max_heights)
chieu cao lon nhat 1.9304
>>> print("chieu cao nho nhat", min_heights)
chieu cao nho nhat 1.8034
>>> height_m.sort(reverse=True)
>>> print("List sau khi sap xep giam dan",height_m)
List sau khi sap xep giam dan [1.9304, 1.8796, 1.8796, 1.8541999999999998, 1.8288, 1.8288, 1.8034, 1.8034]
>>> element=height_m[2]
>>> print("Phan tu thu 3 trong list:",element)
Phan tu thu 3 trong list: 1.8796
