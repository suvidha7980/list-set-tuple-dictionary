myset = {"a", "b", "c", "a"}
print(myset)
print(len(myset))
print(type(myset))

# add item
myset.add("t")
print(myset)

#remove item
myset.remove("a")
print(myset)

#pop item
x = myset.pop()
print(x)
print(myset)

#for loop
for x in myset:
  print(x, end=" ")

#clear item
print(myset.clear())