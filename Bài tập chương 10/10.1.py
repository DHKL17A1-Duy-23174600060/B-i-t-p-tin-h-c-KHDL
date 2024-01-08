# Chương 10
# 10.1
from numbers import Number
def find_max(numbers):
  if all(isinstance(num,Number)for num in numbers):
        max_value= max(numbers)
        return max_value
  else:
      return " Dãy số không hợp lệ"
  def find_min(numbers):
      if all(isinstance(num,Number)for num in numbers):
          min_value=min(numbers)
          return min_value
      else:
          return"Dãy số không hợp lệ"

