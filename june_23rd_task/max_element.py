def find_max(arr):

    max_value = arr[0]

    for num in arr:

        if num > max_value:
            max_value = num

    return max_value


print(find_max([12, 45, 6, 89, 23]))