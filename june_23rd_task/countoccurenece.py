def count_occurrences(arr, target):

    count = 0

    for item in arr:

        if item == target:
            count += 1

    return count


print(count_occurrences([1, 2, 1, 1, 3], 1))