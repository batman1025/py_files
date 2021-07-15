# To write in a file.....we first use write(w) mode or append(a) mode

f= open('new.txt', 'w')
f.write('Please add me to this new text file, I am Avik Khanna') # Adding something will overwrite the previous contents!!!
f.write(input("enter something : "))                                # input function can also be used to write something in the file!!!
f.close()