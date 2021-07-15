def sum(n):
    
        s=0
        i=0
        while i<=n:
            s=s+i
            i+=1
        print(s)        

def sumr(m):
    if m==1:
        return 1
    return m+sumr(m-1)



a=int(input("Enter the n number : "))
sum(a)
b=sumr(int(input("Enter the 2nd n number : ")))
print(b)