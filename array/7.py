

li=[1,2,3,4,5,7]
target=6
for i, value in enumerate(li):
    print(i, value)
    k=value
    if 6-k in li:
        print(i)

