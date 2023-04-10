import itertools

def generate_permutations(lst):
    # Use itertools.permutations to generate all permutations of lst
    permutations = list(itertools.permutations(lst))
    
    # Return the list of permutations
    return permutations

# Example usage
lst = [1, 2, 3]
permutations = generate_permutations(lst)
print(permutations)
