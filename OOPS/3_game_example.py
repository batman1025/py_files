class Remote():
    pass

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

remote1 = Remote()   # calling a class through obj--> object.classname()
player1 = Player()

if(remote1.isLeftPressed()):
    player1.moveLeft()