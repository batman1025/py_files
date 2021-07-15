import random
#  SNAKE WATER GUN GAME or ROCK PAPER SCISSOR

def game(comp,you):
    print("Computer entered "+ comp +" And"+ " You Entered "+ you )

    if comp=='s':
        if you=='w':
            print("You Lose!!")
        elif you=='g':
            print("You Win!!")
        elif you=='s':
            print("Match draw!!")
    elif comp=='w':        
        if you=='g':
            print("You Lose!!")
        elif you=='s':
            print("You Win!!")
        elif you=='w':
            print("Match draw!!")
    elif comp=='g':        
        if you=='s':
            print("You Lose!!")
        elif you=='w':
            print("You Win!!")
        elif you=='g':
            print("Match draw!!")
    

print("Comp's Turn : Snake(s), Water(w), or Gun(g)?  ")
randno= random.randint(1, 3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
    

you=input("Your Turn: Snake(s), Water(w), or Gun(g)?  ")

game(comp,you)
