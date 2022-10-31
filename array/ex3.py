# # Python Program for array rotation

# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 

# Rotation of the above array by 2 will make array

# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
#    arr[] = [3, 4, 5, 6, 7, 1, 2]


arr=[1, 2, 3, 4, 5, 6, 7]
temp=[]
def rotate_arr(arr,n,d):
    
    for i in range(n):
        
        if i<d:
            arr.append(arr[i])

    print(arr)

    arr2=arr[d:n+d]
    print("kkkkkkkkkkk",arr2)

    return arr

arr=[1, 2, 3, 4, 5, 6, 7]
n=len(arr)
d=2


rotate_arr(arr,n,d)

