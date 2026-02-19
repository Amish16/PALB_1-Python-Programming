def find_min_max(arr):
    minimum = maximum = arr[0]
    for num in arr[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return [minimum, maximum]


# Example
arr = [1, 4, 3, 5, 8, 6]
print(find_min_max(arr))
