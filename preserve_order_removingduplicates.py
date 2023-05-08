#lis1=[1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
lis1=['a', 'a', 'b', 'a', 'a', 'c', 'c', 'c', 'd', 'e', 'a', 'b', 'b', 'b']
lis2=[]
for i in lis1:
    if i not in lis2:
        lis2.append(i)
print(lis2)
