class Employee():
    company = "Google"

print(Employee.company)

name = Employee()
Employee.company = "Duck Duck Go"               # This is a class attribute!

avik = Employee()
avni = Employee()
print(avik.company)
print(avni.company)
avik.company="YouTube"                          # These are instance attributes!! for specific object!                        
avni.company="Instagram"                        # These are instance attributes!! for specific object!
print(avik.company)
print(avni.company)


##INSTANCE ATTRIBUTE HAVE HIGER PREFERENCE THAN CLASS ATTRIBUTE!!!!

