# 9.6
import math
def kiem_tra_so_nguyen_to(x):
    if x<2:
        return False
    for i in range (2,int(math.sqrt(x))+1):
        if x % 1==0:
            return True

print(kiem_tra_so_nguyen_to(4))
    