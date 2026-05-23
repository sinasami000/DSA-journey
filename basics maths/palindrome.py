def palindrome(num):
    number = num
    rn = 0
    while num > 0:
        rem = num % 10
        num//=10
        rn = (rn*10) + rem
    print(number,rn)
    return rn == number

print(palindrome(2320))