s = {0, 1, 2, 3, 4, 5}

# Remove 0 from the set
if 0 in s:
    s.remove(0)
print(s)

# Remove 5 from the set
if 5 in s:
    s.remove(5)
print(s)

# Remove 2 from the set
if 2 in s:
    s.remove(2)
print(s)

# Remove 7 from the set (not present in the set)
if 7 in s:
    s.remove(7)
print(s)
