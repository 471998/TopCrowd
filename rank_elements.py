Input=[10, 8, 15, 12, 6, 20, 1]
##Output=[4, 3, 6, 5, 2, 7, 1 ]
opt=[]
new_inp=sorted(Input)
#print(new_inp)
for i in Input:
    if i in new_inp:
        opt.append(new_inp.index(i)+1)
print(opt)
        
