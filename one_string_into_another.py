def checkEditDistance(first, second):
    len_first = len(first)
    len_second = len(second)
    if abs(len_first - len_second) > 1:
        return False
 
    
    edits = 0
    i = j = 0
 
    
    while i < len_first and j < len_second:
        if first[i] != second[j]:
 
            
 
            if len_first > len_second:
                i = i + 1
 
            elif len_first < len_second:
                j = j + 1
 
            
            else:
                i = i + 1
                j = j + 1
 
            
            edits = edits + 1
 
        
        else:
            i = i + 1
            j = j + 1
 
    
    if i < len_first:
        edits = edits + 1
 
    
    if j < len_second:
        edits = edits + 1
 
    
    return edits == 1
 
 
if __name__ == '__main__':
 
    print(checkEditDistance("xyz", "xz"))       # True
    print(checkEditDistance("xyz", "xyyz"))     # True
    print(checkEditDistance("xyz", "xyx"))      # True
    print(checkEditDistance("xyz", "xxx"))      # False
