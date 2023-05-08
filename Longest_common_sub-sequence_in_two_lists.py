from itertools import combinations

def longest_common_subsequence(list1, list2):
    # Generate all combinations of list1
    combs = combinations(list1, min(len(list1), len(list2)))

    # Iterate over the combinations and check if they are subsequences of list2
    lcs = []
    for comb in combs:
        i = 0
        for num in list2:
            if i == len(comb):
                break
            if num == comb[i]:
                lcs.append(num)
                i += 1

    return lcs





list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [6, 7, 5, 6, 7, 8]
print("Original lists:")
print(list1)
print(list2)
print("Longest common subsequence in two lists:")
print(longest_common_subsequence(list1, list2))
print()

### Test case 2
##list1 = [3, 5, 1, 8, 8]
##list2 = [3, 3, 5, 3, 8]
##print("Original lists:")
##print(list1)
##print(list2)
##print("Longest common subsequence in two lists:")
##print(longest_common_subsequence(list1, list2))
##print()
##
### Test case 3
##list1 = [1, 3, 5, 7]
##list2 = [2, 4, 6, 8]
##print("Original lists:")
##print(list1)
##print(list2)
##print("Longest common subsequence in two lists:")
##print(longest_common_subsequence(list1, list2))
##print()
##
### Test case 4
##list1 = [1, 3, 5, 7]
##list2 = [1, 2, 4, 6, 8]
##print("Original lists:")
##print(list1)
##print(list2)
##print("Longest common subsequence in two lists:")
##print(longest_common_subsequence(list1, list2))
