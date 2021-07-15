# Opening a File using python 

f= open('s.txt','r')        #By default the mode is 'r' i.e. read
data= f.read()
# data= f.read(5)           # To read a specific amount of characters starting from the start
print(data)
f.close()                   # closing a file is also important in order to let the file be used somewhere else aswell
                        # we cannot use read more than once in a code