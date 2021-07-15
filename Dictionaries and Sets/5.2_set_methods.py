a=set()

a.add(4)
a.add(5)
a.add((1,2,3))

print(a)

print(len(a))   #this prints the length of the set

a.remove(5)     #will remove the selected obj
a.remove(15)    #will show error as 15 not present in set
print(a)



