def find_index(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1


print(find_index([10, 20, 30, 40], 30))