# Simple function
def fact(n):
    pro=1
    for i in range(n):
        pro=pro*(i+1)
    return pro

    
# Recursive Function
def fact_recur(m):
    if m==1 or m==0:
        return 1
    return m* fact_recur(m-1)

f=fact(5)
print(f)

g=fact_recur(5)
print(g)