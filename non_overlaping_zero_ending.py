lis=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
zeros_lis=[]
non_zeros_lis=[]
for i in lis:
    if i!=0:
        non_zeros_lis.append(i)

    if i==0:
        zeros_lis.append(i)

print(non_zeros_lis+zeros_lis)
