my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)
print(len(my_dict))
print(type(my_dict))

# access item
print(my_dict[2])
print(my_dict.get(1))

#changing item
my_dict[1] = "hello world"
print(my_dict)

#add item
my_dict[3] = "how are you"
print(my_dict)

#pop item
print(my_dict.pop(2))
print(my_dict)

#remove item
print(my_dict.popitem())
print(my_dict)

#clear item
print(my_dict.clear())
print(my_dict)

my_dict = {1: 'hello world', 2: 'ball', 3: 'how are you'}
#printing keys
print(my_dict.keys())
#printing values
print(my_dict.values())
#printing items
print(my_dict.items())
