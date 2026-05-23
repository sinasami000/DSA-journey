N = 4


def leftPyrZero(n):
    for i in range(0,n+1):
        test_case = i%2 != 0
        for k in range(0,i):
            if test_case:
                print(f'{1} ',end="")
                test_case = False
            else:
                print(f'{0} ',end="")
                test_case = True
        print()

def weirdPyramid(n):
    for i in range(n):
        k = 1
        while k <= i+1:
            print(f"{k} ",end="")
            k+=1
        print("- "*((2*n)-(2*i)-2),end="")
        k-=1
        while k > 0:
            print(f"{k} ",end="")
            k-=1
        print()

def numberLeftPyr(n):
    i = 1
    for k in range(n):
        a = 0
        while a <= k:
            print(f"{i} ",end="")
            a+=1
            i+=1
        print()

def letterLeftPyr(n):
    for i in range(n):
        st = 65
        for j in range(i+1):
            print(f"{chr(st)}",end="")
            st+=1
        print()

def ultaABCD(n):
    for i in range(n):
        st = 65
        for j in range(n-i):
            print(f"{chr(st)}",end="")
            st+=1
        print()

def abrABCD(n):
    st = 65
    for i in range(n):
        print(f"{chr(st)}"*(i+1))
        st+=1

def ABCDPyramid(n):
    for i in range(n):
        st = 65
        print(" "*(n-1-i),end="")
        caseVar = 0
        while caseVar <= i:
            print(f"{chr(st)}",end="")
            caseVar+=1
            st+=1
        caseVar-=1
        st-=2
        while caseVar > 0:
            print(f"{chr(st)}",end="")
            caseVar-=1
            st-=1
        print()

def balchal(n):
    starting_char_index = 65 + n - 1
    for i in range(n):
        char_index = starting_char_index-i
        for j in range(i+1):
            print(f"{chr(char_index)} ",end="")
            char_index+=1
        print()

def nineteenth(n):
    # first half
    for i in range(n):
        print("*"*(n-i),end="")
        print(" "*(2*i),end="")
        print("*"*(n-i))
    # second half
    for j in range(n):
        print("*"*(j+1),end="")
        print(" "*(2*n-(2*j)-2),end="")
        print("*"*(j+1))

def twenty(n):
    for i in range(n):
        print("*"*(i+1),end="")
        print(" "*(2*n-(2*i)-2),end="")
        print("*"*(i+1))
    n-=1
    for k in range(n):
        print("*"*(n-k),end="")
        print(" "*(2*k+2),end="")
        print("*"*(n-k))

def hollow(n):
    for i in range(n):
        if i != 0 and i!= n-1:
            for j in range(n):
                if j == 0 or j == n-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        else:
            print("*"*n)

def lastProp(n):
    N = 2*n-1
    for i in range(N):
        for j in range(N):
            a = N-1-j
            b = N-1-i
            minimum_distance = min(i,j,a,b)
            print(f"{n-minimum_distance} ",end="")
        print()
leftPyrZero(N)
weirdPyramid(N)
numberLeftPyr(N)
letterLeftPyr(N)
ultaABCD(N)
abrABCD(N)
ABCDPyramid(N)
balchal(N)
nineteenth(N)
twenty(N)
hollow(N)
lastProp(N)