list1 = ['a','b','c','d','e','f']

list2 = ['d','e','f','g','h']

list3 = list1+list2
print(list3)
for i in list3:
    if i not in list1:
        print("additional values",i)
    if i not in list2:
        print("missing values",i)
