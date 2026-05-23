import math
def armstrong(n):
    num = n
    summation = 0
    while n > 0:
        digit = n%10
        summation+=math.pow(digit,3)
        n//=10
    return summation == num

print(armstrong(153))