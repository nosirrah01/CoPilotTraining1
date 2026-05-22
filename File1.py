def calculate_average(numbers):
    """Return the average of a sequence of numbers. Returns 0 for empty input."""
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    return total / count

def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        # use integer division to get middle index
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1