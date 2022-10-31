# Reversal algorithm for Array rotation

# Given an array arr[] of size N, the task is to rotate the array by d position to the left.

# Examples: 

# Input:  arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3, 4, 5, 6, 7, 1, 2
# Explanation: If the array is rotated by 1 position to the left, 
# it becomes {2, 3, 4, 5, 6, 7, 1}.
# When it is rotated further by 1 position,
# it becomes: {3, 4, 5, 6, 7, 1, 2}

# Input: arr[] = {1, 6, 7, 8}, d = 3
# Output: 8, 1, 6, 7

# approach:
# step1 first reverse d elements :2 1
# step 2 reverse n-d elements : 7 6 5 4 3 
# 2 1  7 6  5 4 3
# now reverse al elements

# 3456712

# function to reverse arr[] from index start to end 



def reverseArray(arr, start, end):
    while start < end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end=end-1

# function to left rotate arr[] of size n by d elements

def leftRotate(arr,d):
    if d==0:
        return 
    n=len(arr)
    # in case the rotating factor is greater than array length
    d=d%n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)

# Function to print an array.

def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=' ')

arr=[1, 2, 3, 4, 5, 6, 7]
n=len(arr)
d=2

leftRotate(arr,d)
printArray(arr)
