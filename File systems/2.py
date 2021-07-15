# Readline function to read

f= open('s.txt', 'r')
data = f.readline()                 # to read the first line of the txt
print(data)
data = f.readline()                 # Using it again will print the next line of the txt and soo onn..
print(data)
f.close()