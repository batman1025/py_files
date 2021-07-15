f= open('poem.txt', 'r')
d= f.read()
if 'twinkle' in d:
    print("twinkle is present")
    
else:
    print("twinkle is not present")
    
f.close()