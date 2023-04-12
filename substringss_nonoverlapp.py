def sub_strings(s):
    if len(s) == 1:
        return ['{' + s + '}']
    substrings = []
    for i in range(1, len(s)):
        for j in sub_strings(s[:i]):
            for k in sub_strings(s[i:]):
                substrings.append(j + k)
    substrings.append('{' + s + '}')
    return substrings

s = 'ABC'
result = sub_strings(s)
for s in result:
    print(s)
