###Bottom-up-approach
##def increasing_nums_bottom_up(n):
##    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
##    for i in range(2, n+1):
##        new_nums = []
##        for num in nums:
##            for j in range(int(num[-1])+1, 10):
##                new_nums.append(num+str(j))
##        nums = new_nums
##    return nums
##
##
##print(increasing_nums_bottom_up(3))


#Top_Down-Approach
def increasing_nums_top_down(n, start='', prev_digit=0):
    if len(start) == n:
        return [start]
    nums = []
    for i in range(prev_digit+1, 10):
        nums += increasing_nums_top_down(n, start+str(i), i)
    return nums


print(increasing_nums_top_down(3))  
