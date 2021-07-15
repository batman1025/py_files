mydict={}

a1=input("Enter Name of friend : ")
a2=input("Enter Their fav language : ")
b1=input("Enter Name of friend : ")
b2=input("Enter Their fav language : ")
c1=input("Enter Name of friend : ")
c2=input("Enter Their fav language : ")
d1=input("Enter Name of friend : ")
d2=input("Enter Their fav language : ")

a={a1,b1,c1,d1}

umydict={
    a1:a2,
    b1:b2,
    c1:c2,
    d1:d2
}
mydict.update(umydict)

print(mydict)