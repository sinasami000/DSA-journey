import random
import time
arr = []
for i in range(20):
    arr.append(random.randint(0,100))

# Find the maximum element in an array

def Maximum(array: list):
    maxValue = array[0]
    for i in array:
        if i > maxValue:
            maxValue = i
    
    return maxValue


# Find the minimum element in an array

def Minimum(array: list):
    minVal = array[0]
    for i in array:
        if i < minVal:
            minVal = i
    
    return minVal



# Calculate the sum of all elements

def sumArr(arr: list):
    summation = 0
    for i in arr:
        summation+=i
    return summation

# Count how many even and odd numbers are in the array

def countEvenAndOdd(arr: list):
    even = 0
    odd = 0
    for i in arr:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return f"even {even} and odd {odd}"

# Reverse an array (without using built-in reverse functions)

def reverse():
    arr = [1,2,3,4,5,8]
    i = 0
    j = len(arr)-1
    while i<j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i+=1
        j-=1
    return arr

# Check if an array is sorted (ascending order)

def isSorted(arr):
    initial = arr[0]
    i = 1
    while i<len(arr):
        if initial > arr[i]:
            return False
        else:
            initial = arr[i]
        i+=1
    return True

# Find the second largest element in an array

def secondLargest(arr):
    lists = {
        "first": max(arr[0],arr[1]),
        "second": min(arr[0],arr[1])
    }
    i = 2
    while i < len(arr):
        if lists["first"] < arr[i]:
            temp = lists["first"]
            lists["first"] = arr[i]
            lists["second"] = temp
        elif lists["first"] > arr[i] and lists["second"] < arr[i]:
            lists["second"] = arr[i]
        i+=1
    print(lists)
    return lists["second"]

# Move all zeros to the end of the array

def moveZeroes():
    arr = [1,2,0,4,8,0,12,54,76,0,43]
    n = len(arr)
    i = 0

    while i < n:
        if arr[i] == 0:
            break
        i+=1
    
    j = i+1
    while j < n:
        if arr[j] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
        j+=1

    return arr

# Find the frequency of each element in the array

def frequency(arr):
    frequencies = {}
    for i in arr:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    print(frequencies)
    return None

# Remove duplicates from a sorted array

def removeDuplicates(arr):
    finalValues = {}
    for i in arr:
        if i not in finalValues:
            finalValues[i] = 1
    return list(finalValues.keys())

# Find the missing number in an array (numbers from 1 to n)

def findMissing(arr,n):
    #  n(n+1)/2
    sumOfN = (n*(n+1))/2
    foundSum = 0
    for i in arr:
        foundSum+=i
    return int(sumOfN-foundSum)

print(arr, Maximum(arr), Minimum(arr), sumArr(arr), countEvenAndOdd(arr), reverse(), isSorted(arr),secondLargest(arr),moveZeroes(), frequency(arr), removeDuplicates(arr),findMissing([1,2,3,5],5))