


lis1=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

result = [x for x in lis1 if (lambda x: x==x[::-1])(x)]

print(result)
