# Check prime or not
n=int(input("Enter Number to check whether it is prime or not : "))
p=True
for i in range(2,n):
    if n%i==0:
        p=False
        break
if p:
    print("number is prime")
else:
    print("number is not prime")