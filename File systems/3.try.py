f = open('new1.txt', 'w')
for i in range(10):                         # Loops can also be used in order to write someting more times!!!
    data= f.write('I am Batman\n')
    print(data)
f.close()