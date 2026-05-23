N = 5

def block(n):
    for i in range(n):
        print("* "*n)

def leftPyramid(n):
    for i in range(n):
        print("* "*(i+1))

def leftNumPyramid(n):
    for i in range(n):
        print(f"{i+1} "*(i+1))

def leftNumPyramidAdvance(n):
    for i in range(n):
        for j in range(i+1):
            print(f"{j+1} ",end="")
        print("")

def leftPyramidReverse(n):
    while n > 0:
        print("* "*n)
        n-=1

def leftPyramidReverseNumber(n):
    while n > 0:
        for i in range(n):
            print(f"{i+1} ",end="")
        print("")
        n-=1

def pyramid(n):
    for i in range(n):
        print("  "*(n-i-1),end="")
        star = 2*(i+1)-1
        print("* "*(star),end="")
        print("")

def reversedPyramid(n):
    for i in range(n):
        print("  "*i,end="")
        print("* "*((2*n)-(2*i)-1))
def doublePyramid(n):
    pyramid(n)
    reversedPyramid(n)

def leftDoublePyramid(n):
    for i in range(n):
        print("* "*(i+1))
    n-=1
    for j in range(n):
        print("* "*(n-j))
block(N)
leftPyramid(N)
leftNumPyramid(N)
leftNumPyramidAdvance(N)
leftPyramidReverse(N)
leftPyramidReverseNumber(N)
pyramid(N)
print()
reversedPyramid(N)
doublePyramid(N)
leftDoublePyramid(N)