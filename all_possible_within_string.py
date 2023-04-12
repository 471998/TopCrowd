def palindromic_substrings(string):
    n = len(string)
    result = []

    for i in range(n):
        for j in range(i+1, n+1):
            substring = string[i:j]
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                result.append(substring)

    return result
string = "google"
print(palindromic_substrings(string))
