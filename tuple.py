mytuple = ("a", "b", "c", "b")
print(mytuple)
print(len(mytuple))
print(type(mytuple))

#access tuple
print(mytuple[1])

#change tuple items
x = list(mytuple)
x[1] = "hello"
print(tuple(x))

#add item
x = list(mytuple)
x.append("world")
print(tuple(x))

#remove item
x = list(mytuple)
x.remove("b")
print(tuple(x))

#foor loop
for x in mytuple:
  print(x, end=" ")
print(" ")

#count item
print(mytuple.count("b"))

#index item
print(mytuple.index("b"))
