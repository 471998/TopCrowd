def quickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        # Select the last element as the pivot
        pivot = arr[n-1]
        # Initialize the left and right sub-arrays
        left = []
        right = []
        # Partition the array around the pivot
        for i in range(n-1):
            if arr[i] <= pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        # Recursively sort the left and right sub-arrays
        return quickSort(left) + [pivot] + quickSort(right)
        
# Example usage
arr = [10, 7, 8, 9, 1, 5]
sortedArr = quickSort(arr)
print("Sorted array:", sortedArr)
