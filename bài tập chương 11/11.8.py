Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def has_lucky_numbers(nums):
...     for num in nums:
...         if num % 7 ==0:
...             return True
...         return False
... nums=[2,6,7,9]
SyntaxError: invalid syntax
>>> nums=[2,6,7,9]
>>> print(has_lucky_number(nums))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(has_lucky_number(nums))
NameError: name 'has_lucky_number' is not defined
