# we will have to find the summation of N numbers using recursion.
# This problem can be solved in two different approach. First one is parameterised way and the second one is functional way.

# parameterised way:

def parameterised(i,sum):
    if i < 1:
        print(sum)
        return
    parameterised(i-1,sum+i)

parameterised(20,0)

# functional way:

def functional(n):
    if n < 0:
        return 0
    return n + functional(n-1)

print(functional(20))


# finding factorial in functional way

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(20))