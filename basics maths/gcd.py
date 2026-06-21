import math
def GCD(n1,n2):
    sortest = min(n1,n2)
    gcd = 1
    for i in range(1,sortest+1):
        if n1%i == 0 and n2%i == 0:
            gcd = i
    return gcd

print(GCD(10,20))

# Euclidean algorithm: GCD(a,b) will be GCD(a-b,b) where a>b

def GCDWithEuclidean(n1,n2):
    while n1 > 0 and n2 > 0:
        if n1>n2:
            n1%=n2
        else:
            n2%=n1

    return max(n1,n2)
print(GCDWithEuclidean(10,50))