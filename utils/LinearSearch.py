def linear_search(array, target) -> int:
    for i in range(len(array)):
        if array[i] == target:
            return i