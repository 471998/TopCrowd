def longest_palindrome(s):
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i+1, n+1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1] and len(sub_str) > len(longest):
                longest = sub_str
    return longest
s="abcbcaed"
print(longest_palindrome(s))
