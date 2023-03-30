Input=[9, -3, 5, -2, -8, -6, 1, 3]
pos_li=[]
neg_li=[]
for i in Input:
    if i>0:
        pos_li.append(i)
    elif i<0:
        neg_li.append(i)
print(neg_li+pos_li)
