def print_largest_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    start_index = 0
    end_index = 0
    current_start_index = 0
    
    # iterate over array
    for i in range(1, len(arr)):
        # update current sum
        if current_sum + arr[i] > arr[i]:
            current_sum = current_sum + arr[i]
        else:
            current_sum = arr[i]
            current_start_index = i
            
        # update max sum and subarray indices
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = current_start_index
            end_index = i
    
    
    print("Largest subarray: ", arr[start_index:end_index+1])
arr = [1, -2, 3, 4, -5, 8]
print_largest_subarray(arr)
