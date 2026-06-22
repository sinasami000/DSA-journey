# A function that calls itself on a specific condition is called a recursion function.

def f(name):
    print(f"I love you, {name}")
    f(name)

f("myself")

num = 0

def count():
    global num
    print(num)
    num+=1
    if num < 101: # a certain condition should be given, otherwise the recursion will go on infinitely and break.
        count()

count()