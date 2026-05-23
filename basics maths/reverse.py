def reverseNum(num):
    final = 0
    while num > 0:
        reminder = num % 10
        num = num//10
        final = (final*10)+reminder
    return final

print(reverseNum(123))