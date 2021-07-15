def great(a,b,c):
    if (a>b and a>c):
        print("a is the greatest")
        
    elif (b>c):
        print("b is the greatest")
        
    else:
        print("c is the greatest")
        
        
x=int(input("Enter The numbers : "))
y=int(input("Enter The numbers : "))
z=int(input("Enter The numbers : "))

great(x, y, z)