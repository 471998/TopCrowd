def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = [5, 2, 4, 7, 1, 3]
x = 7
result = linear_search(arr, x)
if result == -1:
    print(f"{x} not found in array")
else:
    print(f"{x} found at index {result}")
