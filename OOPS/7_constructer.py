class Employee:
    company = "Google"
    def getsalary(self):
        print(self.salary, "\n")
        
    def __init__(self, name, salary, unit):
        self.name= name
        self.salary= salary
        self.unit= unit
        print("An Employee in created!")
        
    @staticmethod                       # Used when self not required!!
    def greet():
        print("Good Morning, Employee")
        
    def getDetails(self):
        print(f"The Name of the Employee is : {self.name}")
        print(f"The Salary of the Employee is : {self.salary}")
        print(f"The Unit of the Employee is : {self.unit}")
        
avik = Employee("Avik", 200, "cyber sec")
# avni = Employee("Avni", 300, "A I")

# avik.salary= input("Enter salary for Avik : ")
# avni.salary= input("Enter salary for Avni : ")
# avik.getsalary()
# avni.getsalary()
# avik.greet()
# avni.greet()
avik.getDetails()
# avni.printDetails()