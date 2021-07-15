def pat(n):                     # using nested loop
    for i in range(1,n+1):
        for j in range(n+1,i,-1):
            print("*", end="")
        print("\r")
        
def pat1(m):                    # using single loop
    for i in range(m):
        print("*"*(m-i))
        
        
        

a=int(input("Enter the n number of first line : "))
pat(a)
b=int(input("Enter the n number of first line : "))
pat1(b)