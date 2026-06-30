def binary_search(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search(arr, mid + 1, high, key)
    else:
        return binary_search(arr, low, mid - 1, key)

arr = [5,10,15,20,25,30,35]
print(binary_search(arr,0,len(arr)-1,30))

