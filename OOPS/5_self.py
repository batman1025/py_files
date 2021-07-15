class Employee:
    company = "Google"
    def getsalary(self):
        print(self.salary, "\n")
        
avik = Employee()
avni = Employee()

avik.salary= input("Enter salary for Avik : ")
avni.salary= input("Enter salary for Avni : ")
avik.getsalary()
avni.getsalary()