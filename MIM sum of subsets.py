def sum_of_subsets(arr, target):
    result = []

    def backtrack(index, current_sum, subset):
        if current_sum == target:
            result.append(subset[:])
            return

        if current_sum > target or index == len(arr):
            return

        # Include current element
        subset.append(arr[index])
        backtrack(index + 1, current_sum + arr[index], subset)

        # Exclude current element
        subset.pop()
        backtrack(index + 1, current_sum, subset)

    backtrack(0, 0, [])

    if result:
        print("Subsets with sum", target, ":")
        for s in result:
            print(s)
    else:
        print("No subset found.")

arr = [5, 10, 12, 13, 15, 18]
target = 30

sum_of_subsets(arr, target)
