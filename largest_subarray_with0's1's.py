#FIND THE LARGEST SUBARRAY HAVING AN EQUAL NUMBER OF 0’S AND 1’S
 
def findLargestSubarray(arr):
    # initialize variables
    max_len = 0
    sum_dict = {0: -1}
    sum_val = 0
    start = 0
    end = 0

    # iterate over the array
    for i in range(len(arr)):
        # update the running sum
        if arr[i] == 0:
            sum_val -= 1
        else:
            sum_val += 1

        # check if we've seen this sum before
        if sum_val in sum_dict:
            # update the max length and subarray indices if applicable
            curr_len = i - sum_dict[sum_val]
            if curr_len > max_len:
                max_len = curr_len
                start = sum_dict[sum_val] + 1
                end = i
        else:
            # add the sum to the dictionary
            sum_dict[sum_val] = i

    return arr[start:end+1]
arr = [0, 1, 0, 1, 1, 1, 0, 0]
largest_subarray = findLargestSubarray(arr)
print(largest_subarray)
