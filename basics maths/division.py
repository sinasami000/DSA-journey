import math
def division(n):
    for i in range(round(math.sqrt(n))):
        if n%(i+1) == 0:
            print(f"{i+1}, ",end="")
            if (i+1) != math.sqrt(n):
                print(f"{round(n/(i+1))}, ",end="")

division(36)
