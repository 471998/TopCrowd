def majority_element(li):
    count=0
    for i in range(0,len(li)):
        for j in range(i+1):
            if li[i]==li[j]:
                count+=1
    return li[i]
li=[1,2,3,4,2,1,5,6,4,1]
print(majority_element(li))
        
       
