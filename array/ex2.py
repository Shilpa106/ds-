# Python Program to find largest element in an array
# Difficulty Level : Easy
# Last Updated : 21 Jul, 2022
# Read
# Discuss

# Given an array, find the largest element in it.

# Input : arr[] = {10, 20, 4}
# Output : 20

# Input : arr[] = {20, 10, 20, 4, 100}
# Output : 100

a=[20, 10, 20, 4, 100]
# mx=max(a)
# print(mx)

mx=0
for i in a:
    if i>mx:
        mx=i
print(mx)