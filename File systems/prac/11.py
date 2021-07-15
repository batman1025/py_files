import os

oldname= 'log2.txt'
newname= 'renamed.txt'

with open(oldname) as f:
    content = f.read()
    
with open(newname, 'w') as f:
    f.write(content)
    
os.remove(oldname)