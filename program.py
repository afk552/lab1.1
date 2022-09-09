import random

arr = []
for i in range (3):
    print (i)
    arr.append(random.randint(1,100))

res = sum(arr)

print (res)
