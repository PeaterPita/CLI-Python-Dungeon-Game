from Tiles import *

    


class Player(tile):
    def __init__(self, posRow, posCell):
        super().__init__(icon="^", color="magenta")
        self.posRow = posRow
        self.posCell = posCell
    
    
    def move(self, amountRow: int = 0, amountCell: int = 0) -> None:
        newPosRow = self.posRow - amountRow
        newPosCell = self.posCell + amountCell
        
        nextTile = game.currentRoom.getTile(
            row=newPosRow,
            cell=newPosCell
            )
        if nextTile.obstruction: return
        
        if isinstance(nextTile, door):
            print("Found door")
            if nextTile.linksTo:
                game.swapRoom(nextTile.linksTo)
            elif not nextTile.linksTo:
                nextTile.linksTo = room()
                nextTile.linksTo.editDoors([nextTile.direction, game.currentRoom])
                game.swapRoom(nextTile.linksTo)
            return
                
                
        game.currentRoom.setTile(row=self.posRow, cell=self.posCell, obj=tile())
        
        game.currentRoom.setTile(row=newPosRow, cell=newPosCell, obj = self)
        self.posRow = newPosRow
        self.posCell = newPosCell     



        

class Game():
    def __init__(self):
        self.map = []
        self.startingroom = room(size=8, name="Starting Room", coords=(0,0))
        self.currentRoom = self.startingroom
        
        self.player = Player(posRow= self.currentRoom.getMiddle(), posCell=self.currentRoom.getMiddle())
        self.currentRoom.setTile(row = self.player.posRow, cell = self.player.posCell, obj=self.player)
        
    def run(self):
        while True:
            self.currentRoom.printRoom()
            self.action()
            
            
    def swapRoom(self, newRoom):
        self.currentRoom.setTile(row=self.player.posRow, cell=self.player.posCell, obj=tile())
        self.currentRoom = newRoom
        
        
        self.player.posRow = newRoom.getMiddle()
        self.player.posCell = newRoom.getMiddle()
        
        
        self.currentRoom.setTile(row=self.player.posRow, cell=self.player.posCell, obj = self.player)
        
    
    
    def action(self):
        while True:
            print("What will you do?: (type 'help' for commands)")
            match input().lower():
                case "w":
                    self.player.seticon("^")
                    self.player.move(amountRow= 1)
                case "a":
                    self.player.seticon("<")
                    self.player.move(amountCell= -1)
                case "s":
                    self.player.seticon("⌄")
                    self.player.move(amountRow= -1)
                case "d":
                    self.player.seticon(">")
                    self.player.move(amountCell= 1)
                case "help":
                    pass
                case "quit":
                    quit()
                case _:
                    print("Unknown Move")
                    continue
            break
        






if __name__ == "__main__":
    game = Game()
    game.run()