def binary_search_recursive(arr, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search_recursive(
            arr,
            target,
            mid + 1,
            right
        )

    else:
        return binary_search_recursive(
            arr,
            target,
            left,
            mid - 1
        )
        
leaderboard = [1200, 1450, 1600, 1750, 1800, 1920, 2050, 2200]

score_to_find = 1800

position = binary_search_recursive(
    leaderboard,
    score_to_find,
    0,
    len(leaderboard) - 1
)

print(f"Score {score_to_find} is at leaderboard rank {position + 1}")