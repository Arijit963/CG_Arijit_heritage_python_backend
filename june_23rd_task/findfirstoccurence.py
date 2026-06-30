def first_occurrence(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1


print(first_occurrence([5, 8, 8, 10], 8))