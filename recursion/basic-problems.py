# part two: basic recursion problem

# problem 1: print your name N times

def printing_name(i,k,name):
    if i > k:
        return
    print(name)
    printing_name(i+1,k,name)

printing_name(1,5,"Adnan")

# problem 2: print linearly from i to N

def i_to_N(j,N):
    if j > N:
        return
    print(j)
    i_to_N(j+1,N)

i_to_N(1,30)

# problem 3: print linearly from N to i

def N_to_i(N,i):
    if N < i:
        return
    print(N)
    N_to_i(N-1,i)

N_to_i(5,1)

# problem 4: print linearly from i to N by using backtracking.

def increasingOrderBacktrack(i,N):
    if i < 1:
        return
    increasingOrderBacktrack(i-1,N)
    print(i)
print("------------")
increasingOrderBacktrack(10,10)


# problem 5: print linearly from N to i by using backtracking.

def decreasingOrderBacktrack(i,N):
    if i > N:
        return
    decreasingOrderBacktrack(i+1,N)
    print(i)

print("------------")
decreasingOrderBacktrack(1,5)