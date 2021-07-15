class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of the programmer is {self.name} and the company associated with is {self.product}")

avik = Programmer(input("Enter Name : "), input("Enter Product : "))
avni = Programmer(input("Enter Name : "), input("Enter Product : "))
avik.getInfo()
avni.getInfo()
        