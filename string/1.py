# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.

s = ["h","e","l","l","o"]

# # m1
# print(s[-1::-1])

# # m2
# for i in range(1,len(s)+1):
#     print(s[-i])

# M3

def reverse_func(x): 
    y=x[-1::-1]
    return y

x=["h","e","l","l","o"]
print(reverse_func(x))