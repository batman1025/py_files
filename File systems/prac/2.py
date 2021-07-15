#  hiscore shittt!!!
def game(n):
    sum = 10 + n
    return sum




a=int(input('''welcome to the game of addition!!
      please enter a number to be added to 10 : '''))

b=game(a)

f=open('hiscore.txt', 'r')
g= f.read()

if g=='':
    with open('hiscore.txt', 'w') as f:
        u= f.write( str(b))
    
elif int(g)<b:
    with open('hiscore.txt', 'w') as f:
        u= f.write( str(b))
else:
    pass

f.close()

