def find_first_repeating_element_index(lst):
    count = {}
    for i, elem in enumerate(lst):
        if elem in count:
            return count[elem]
        else:
            count[elem] = i
    return None  


lst = [1, 2, 3, 4, 5, 2, 6, 7, 8]
print(find_first_repeating_element_index(lst))  
