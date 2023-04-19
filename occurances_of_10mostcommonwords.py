text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit corporation that holds the intellectual property rights behind the Python programming language.
We manage the open source licensing for Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American PyCon
conference annually, support other Python conferences around the world, and fund Python related development
with our grants program and by funding special projects.""".split()
#print(text)
new={i:text.count(i) for i in text}
#print("Dictinaryyyy",new)
out={k: v for k, v in sorted(new.items(), key=lambda item: item[1])}
print("valuesortedddd",out)
keys = list(out.keys())
last_10_keys = keys[-10:]
print(last_10_keys)
#print("valuesortedddd",out)

