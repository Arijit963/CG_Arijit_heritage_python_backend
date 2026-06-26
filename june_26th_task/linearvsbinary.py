import time

arr = list(range(100000))
key = 99999


# Linear Search
start = time.time()

for i in range(len(arr)):
    if arr[i] == key:
        break

linear_time = time.time() - start


# Binary Search
start = time.time()

low = 0
high = len(arr)-1

while low <= high:
    mid = (low+high)//2

    if arr[mid] == key:
        break
    elif arr[mid] < key:
        low = mid+1
    else:
        high = mid-1

binary_time = time.time() - start


print("Linear Search Time :", linear_time)
print("Binary Search Time :", binary_time)
