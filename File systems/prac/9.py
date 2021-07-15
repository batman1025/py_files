with open(input("Enter the first file : ")) as f:
    content1= f.read()

with open(input("Enter the second file : ")) as f:
    content2= f.read()
    
    
if content1 == content2:
    print("Yes the text present in these both files are same!!!")
else:
    print("No the text present in these both files are not same!!!")