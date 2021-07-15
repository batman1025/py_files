class Calculator:
    def __init__(self, num):
        self.number = num
        
    def sqr(self):
        print(f"The Square of the number entered is {self.number**2}")
        
    def cube(self):
        print(f"The Cube of the number entered is {self.number**3}")
        
    def sqRoot(self):
        print(f"The Square Root of the number entered is {self.number**0.5}" )
        
    
num1 = Calculator(int(input("Enter a Number : ")))
num1.sqr()
num1.cube()
num1.sqRoot()