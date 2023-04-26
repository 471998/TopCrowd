lst = [2, 4, 6, 9, 11]
n = 2

result = [(lambda x: x * n)(x) for x in lst]

print("Result:")
print(*result)

lst = [2, 4, 6, 9, 11]
n = 2

result = list(map(lambda x: x * n, lst))

print("Result:")
print(*result)

