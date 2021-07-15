#  .strip() function removes the extra spaces at beginning and the end of the string

def rands(s,w):
    n=s.replace(w,"")
    print(n.strip())
    
    
    
    
b=input("Enter a string : ")
c=input("Enter a word to be removed : ")

rands(b,c)
