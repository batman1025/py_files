#  inches to cms

def conv(n):
    return n * 2.54


a=int(input("Enter value in inches : "))
b=conv(a)
print(f"The value entered in cms will be {b}")
