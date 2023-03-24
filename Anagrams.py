
def Anagrams(li):
    dictionary = {}
    for word in li:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in dictionary:
            dictionary[sortedWord] = [word]
        else:
            dictionary[sortedWord] += [word]
    return [dictionary[i] for i in dictionary]


li = ['car','bat','arc','opp','cat','act']
   # Call to function to Solve and group Anagrams
print(Anagrams(li))
