'''
PascleCase - something which is written in this format-- AvikKhannaAvniVerma


camelCase - something which is written in this format-- avikKhannaAvniVerma

'''
class Number:
    def sum(self):
        return self.a + self.b
    

num = Number()
num.a= int(input("Enter first number : "))
num.b= int(input("Enter second number : "))
s= num.sum()
print(s)
