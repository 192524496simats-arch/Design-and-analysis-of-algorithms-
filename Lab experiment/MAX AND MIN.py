def max_min(arr, low, high):
    # Only one element
    if low == high:
        return arr[low], arr[low]

    # Two elements
    elif high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    max1, min1 = max_min(arr, low, mid)
    max2, min2 = max_min(arr, mid + 1, high)

    # Conquer
    maximum = max(max1, max2)
    minimum = min(min1, min2)

    return maximum, minimum


# Input
arr = list(map(int, input("Enter the elements: ").split()))

# Function call
maximum, minimum = max_min(arr, 0, len(arr) - 1)

print("Maximum element:", maximum)
print("Minimum element:", minimum)
