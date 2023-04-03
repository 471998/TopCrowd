def combine_dicts(d1, d2):
    # Create an empty dictionary to store the result
    result = {}
    
    # Iterate over the keys in d1 and add the values for common keys
    for key, value in d1.items():
        if key in d2:
            result[key] = value + d2[key]
        else:
            result[key] = value
    
    # Iterate over the keys in d2 and add any keys that are not already in the result
    for key, value in d2.items():
        if key not in result:
            result[key] = value
    
    return result

# Example usage
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

combined = combine_dicts(d1, d2)
print(combined)


##from collections import Counter
##
##def combine_dicts(d1, d2):
##    # Use Counter to add the values for common keys
##    result = Counter(d1) + Counter(d2)
##    
##    return result
##
### Example usage
##d1 = {'a': 100, 'b': 200, 'c':300}
##d2 = {'a': 300, 'b': 200, 'd':400}
##
##combined = combine_dicts(d1, d2)
##print(combined)
##
