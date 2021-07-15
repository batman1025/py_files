mydict={
    "Fast": "In a Quick manner",
    "Avik": "Is The Batman",
    "Marks": [1,2,3,6,5,4],
    "mydict2":{"Avik":"Footballer"}  #nested dictionaries
    }

print(mydict['Fast'])    
print(mydict['Avik'])    
print(mydict['Marks'])    
mydict['Marks']=[66,78,89]          # this means dictionaries are mutable or changable
print(mydict['Marks'])    
print(mydict['mydict2'])    
print(mydict['mydict2']['Avik'])    
