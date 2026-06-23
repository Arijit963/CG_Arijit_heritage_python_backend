def find_all_occurrences(arr, target):

    positions = []

    for i in range(len(arr)):

        if arr[i] == target:
            positions.append(i)

    return positions


print(find_all_occurrences([1, 2, 1, 3, 1], 1))