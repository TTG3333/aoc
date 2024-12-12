with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

maxX = len(lines[0])
maxY = len(lines[1])
def checkCoords(x, y):
    return x >= 0 and x < maxX and y >= 0 and y < maxY

around = [[1, 0], [0, 1], [-1, 0], [0, -1]]
class Region:
    def __init__(self, plant):
        self.plots = set()
        self.perimeterPlots = set()
        self.sides = 0
        self.plant = plant
    
    def __str__(self):
        toReturn = f"Plant: {self.plant}\n"
        toReturn += f"Area: {len(self.plots)}\n"
        toReturn += f"Sides: {self.sides}\n"
        toReturn += f"{len(self.perimeterPlots)} perimeter plots"
        return toReturn

    def populate(self, x, y, checked):
        checked.add((x, y))
        self.plots.add((x, y))
        for xOff, yOff in around:
            newX = x + xOff
            newY = y + yOff
            if checkCoords(newX, newY) and lines[newY][newX] == self.plant:
                if (newX, newY) not in checked:
                    self.populate(newX, newY, checked)
            else: # We have a plot boundary
                self.perimeterPlots.add((x, y))

    def computeSides(self): # Each time we turn, we have a new side
        checked = set()
        for plot in self.perimeterPlots:
            for direction in range(4): # Direction is the direction to look for plots outside the region, and we traverse the plot 90 degrees clockwise from this direction
                inLoop = False
                while (plot, direction) not in checked:
                    newX, newY = (plot[i] + around[direction][i] for i in range(2))
                    if (newX, newY) in self.plots: # The plot in direction direction is a part of the region
                        if inLoop: # Turn 90 degrees counterclockwise and move forwards one space
                            checked.add((plot, direction))
                            plot = (newX, newY)
                            direction = (direction-1)%4
                            self.sides += 1
                        else:
                            break
                    else:
                        checked.add((plot, direction))
                        forwardDirection = (direction+1)%4
                        forX, forY = (plot[i] + around[forwardDirection][i] for i in range(2))
                        if (forX, forY) not in self.plots: # Just turn right
                            direction = forwardDirection
                            self.sides += 1
                        else:
                            plot = (forX, forY)
                    inLoop = True

total = 0
checked = set()
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if (x, y) not in checked:
            region = Region(char)
            region.populate(x, y, checked)
            region.computeSides()
            total += region.sides * len(region.plots)
print(total)