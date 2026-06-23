def has_duplicates(arr):

    for i in range(len(arr)):

        for j in range(i + 1, len(arr)):

            if arr[i] == arr[j]:
                return True

    return False


print(has_duplicates([1, 2, 3, 2]))