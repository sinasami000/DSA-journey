import math
def extract(num):
    nums = []
    while num > 0:
        nums.append(num%10)
        num = num//10
    nums.reverse()
    return nums


def countDigit(n):
        return int(math.log10(n)+1) 

print(countDigit(1235))