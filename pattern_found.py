def checkPattern(word, pattern):
    if not word or not pattern or len(word) < len(pattern):
        return False
    prev = None
    for curr in pattern:
        firstIndex = word.find(curr)
        if firstIndex == -1 or (prev and word.rfind(prev) > firstIndex):
            return False
        prev = curr

    return True
 
if __name__ == '__main__':
    word = 'Techie Delight'
    pattern = 'el'
    if checkPattern(word, pattern):
        print('Pattern found')
    else:
        print('Pattern not found')
 
