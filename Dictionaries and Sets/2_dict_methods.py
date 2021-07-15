mydict={
    "fast": "In a Quick manner",
    "avik": "Is The Batman",
    "marks": [1,2,3,6,5,4],
    "mydict2":{"Avik":"Footballer",},        #nested dictionaries
    1:2                                    
    }

# Dictionary methods
print(mydict.keys())        # shows keys in form of list but is still a dict_key// to change we could use typecasting "list(mydict.keys*())"
print(mydict.values())      # show values in form of list but is still a dict_values// to change do the same
print(mydict.items())       # show everything in the dictionary in form of list in tuple but is still a dict_item..//rest same
print(mydict)
umydict={
    "Avni": "Girlfriend",
    "sahil": "Bestfriend",
    "avik":  "The Batman"           #repeating key will change the value from the initial key
}
mydict.update(umydict)          #to add contents at the end of the dict in pairs
print(mydict)
print(mydict.get("avik"))       # prints value assossiated with harry
print(mydict["avik"])          # same

# The Difference between .get and [] syntax
print(mydict.get("avik2"))       # this will return none as there is avik2 not present in the dictionary    
print(mydict["avik2"])          # this will throw error as avik2 is not present in the dictionary
