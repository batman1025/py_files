# creating an empty set

a=set()
print(type(a))



# adding values to the empty set

a.add(4)
a.add(5)

a.add([1,2])    # cannot be added as lists and dictionary are un hashable moreover can be changed.    
a.add((1,2))    # but tuples can be added to sets
a.add({1:2})    # cannot be added as lists and dictionary are un hashable moreover can be changed.

print(a)


