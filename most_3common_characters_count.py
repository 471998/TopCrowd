text=" lkseropewdssafsdfafkpwe"
new={i:text.count(i) for i in text}
#print("Dictinaryyyy",new)
out={k: v for k, v in sorted(new.items(), key=lambda item: item[1])}
print("valuesortedddd",out)
keys = list(out.items())
last_10_items = keys[-3:]
print(last_10_items)
#print("valuesortedddd",out)
