#Write a Python program to get a single string from two given strings, separated by a space and
#swap the first two characters of each string(python)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# swap the first two characters of each string
string1_swapped = string2[:2] + string1[2:]
string2_swapped = string1[:2] + string2[2:]

# concatenate the two strings with a space in between
result = string1_swapped + ' ' + string2_swapped

print("Result:", result)
