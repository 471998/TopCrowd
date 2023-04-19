lis=['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']
new={i:lis.count(i) for i in lis}
print(new)
out=max(new,key=new.get)
print(out)
