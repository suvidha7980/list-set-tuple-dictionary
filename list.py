mylist = ["a", "b", "c", "a"]
print(mylist)
print(len(mylist))
print(type(mylist))

#access item
print(mylist[1])

#change item
mylist[1] = "hello"
print(mylist)

#add item
mylist.append("world")
print(mylist)

#insert item
mylist.insert(1, "hi")
print(mylist)

#remove list
mylist.remove("a")
print(mylist)

#pop item
mylist.pop(1)
print(mylist)

mylist.pop()
print(mylist)


# for loop
for x in mylist:
  print(x,end=" ")

#sort item
print(mylist.sort())