class Lists():
    def identity(self):
        create= {}
        for j in range(self.n):
            create.update({self.a:self.b,
                           self.a:self.b})
        print(create)
    # def new(self):
    #     for j in self.i:
    #         add=
    

fun = Lists()    
fun.n= int(input("Enter how many identities to be added : "))
for i in range(fun.n):
    fun.a=input("enter a name : ")
    fun.b=input("enter a quality : ")
fun.identity()

# print(d)

