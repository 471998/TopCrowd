string = "Mallika"
char = input("enter character")

check_starts_with_char = lambda x: True if x.startswith(char) else False

print(check_starts_with_char(string))
