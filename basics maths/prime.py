def prime(n):
    i = 2
    while i <= n/2:
        if n%i == 0:
            return False
        i+=1
    return True
print(prime(80))

# optimized version