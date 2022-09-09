import random

arr = []
for i in range (3):
    arr.append(random.randint(1,100))

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

res = sum(arr)

print (res)
