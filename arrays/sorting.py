import random
# Bubble sort 

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):

        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr
arr = [random.randint(0, 10) for _ in range(10)]
print(arr)
print(bubble_sort(arr))