from Util import Color

class tile():
    def __init__(self, 
                 name: str = "blank", 
                 icon: str = " ", 
                 color: str = "white",
                 obstruction: bool = False):
        self.obstruction = obstruction
        self.name = name
        self.color = color
        
        self.seticon(icon)
        
        
    def seticon(self, newIcon: str):
        self.icon = Color[self.color.upper()].value[1] + newIcon + Color.CLEAR.value[1]
        

class door(tile):
    def __init__(self, direction):
        super().__init__(icon = "/", color = "yellow", name = "door")
        self.linksTo = None
        self.direction = direction
        
    def setLinksTo(self, room):
        self.linksTo = room
        

        
class wall(tile):
    def __init__(self):
        super().__init__(name = "wall", icon = "#", obstruction = True)
        
        
        
        
class room():
    def __init__(self, size: int = 8, name: str | None = None, coords: tuple = (0,0)):
        self.innerSize = size
        self.outerSize = size + 1
        self.name = name
        self.coords = coords
        self.doors = {}
        
        
        self.grid = [ ["?" for _ in range(self.outerSize)] for _ in range(self.outerSize) ]
        self.makeRoom()
        
    def editDoors(self, camefrom: list = None):
        match camefrom[0]:
            case "up":
                self.doors["down"].setLinksTo(camefrom[1])
                self.coords = (camefrom[1].coords[0], camefrom[1].coords[1] + 1)
                
            case "right":
                self.doors["left"].setLinksTo(camefrom[1])
                self.coords = (camefrom[1].coords[0] + 1, camefrom[1].coords[1])
            case "down":
                self.doors["up"].setLinksTo(camefrom[1])
                self.coords = (camefrom[1].coords[0], camefrom[1].coords[1] - 1)
            case "left":
                self.doors["right"].setLinksTo(camefrom[1])
                self.coords = (camefrom[1].coords[0] - 1, camefrom[1].coords[1])
        self.name = self.name or f"[ {self.coords[0]}, {self.coords[1]} ]"

        
    def makeRoom(self):
        for row in range(self.outerSize):
            for cell in range(self.outerSize):
                doorDirection = None
                
                # If row is the TOP of the grid or the BOTOM
                if row == 0 or row == (self.outerSize - 1):
                    self.grid[row][cell] = wall()
                    
                    # If cell is in the middle:
                        # TOP MIDDLE
                        #  BOTTOM MIDDLE
                    if cell == self.getMiddle():
                        if row == 0:
                            doorDirection = "up"
                        elif row == (self.outerSize - 1):
                            doorDirection = "down"
                        else:
                            print("Error in door creation")
                        tempdoor = door(direction=doorDirection)
                        self.doors[doorDirection] = tempdoor
                        self.grid[row][cell] = tempdoor
                    continue
                if cell == 0 or cell == (self.outerSize - 1):
                    self.grid[row][cell] = wall()
                    
                    if row == self.getMiddle():
                        if cell == 0:
                            doorDirection = "left"
                        elif cell == (self.outerSize - 1):
                            doorDirection = "right"
                        else:
                            print("Error in door creation")
                            
                        tempdoor = door(direction=doorDirection)
                        self.doors[doorDirection] = tempdoor
                        self.grid[row][cell] = tempdoor
                        
                    continue
                
                self.grid[row][cell] = tile()
                
        
    def printRoom(self):
        if self.name:
            print(self.nameEmbleshiment())
        for row in self.grid:
            print(f"{' '.join(tile.icon for tile in row)}")
            
    
    def nameEmbleshiment(self):
        EmbLength = (self.outerSize * 2) - 1 - len(self.name) 
        return f"{"~" * EmbLength} {self.name} {"~" * EmbLength}"
            
    def setTile(self, row: int, cell: int, obj):
        self.grid[row][cell] = obj
        
    def getTile(self, row, cell):
        return self.grid[row][cell]
        
    def getMiddle(self) -> int:
        return round(self.outerSize / 2)
        
