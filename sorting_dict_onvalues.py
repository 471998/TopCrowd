original_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

sorted_list = sorted(original_list, key=lambda x: x['key']['subkey'], reverse=True)

print("Original List: ")
print(original_list)

print("Sorted List: ")
print(sorted_list)
