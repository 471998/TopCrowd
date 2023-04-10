def circularly_identical(list1, list2):
    # Check if the lists have the same length
    if len(list1) != len(list2):
        return False
    
    # Concatenate the first list to itself to create a circular version
    circular_list1 = list1 + list1
    
    # Iterate through all possible starting points in the circular list
    for i in range(len(list1)):
        if circular_list1[i:i+len(list1)] == list2:
            return True
    
    
    return False


list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print("Compare list1 and list2")
print(circularly_identical(list1, list2))  # True

print("Compare list1 and list3")
print(circularly_identical(list1, list3))  # False
