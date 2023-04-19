elements = ['p', 'q', 'r', 's']
counts = [4, 2, 0, -2]

output = []
for i, count in enumerate(counts):
    if count > 0:
        output += [elements[i]] * count

print(output)
