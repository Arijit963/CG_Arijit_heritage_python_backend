def find_min(arr):

    min_value = arr[0]

    for num in arr:

        if num < min_value:
            min_value = num

    return min_value


print(find_min([12, 45, 6, 89, 23]))