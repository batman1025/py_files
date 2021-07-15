def pat(n):
  for i in range(1,n):
    for j in range(1,i+1):
      print("*",end="")
    print("\r")



n=input("Enter Number: ")
n=int(n)
pat(n)    