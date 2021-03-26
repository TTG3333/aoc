with open("Input.txt", "tr") as F:
    instructions = F.read().splitlines()

position = [0, 0]
angle = 90

def move(pos, moveAngle, distance):
    newPos = pos
    if moveAngle == 0:
        newPos[1] += distance
    elif moveAngle == 90:
        newPos[0] += distance
    elif moveAngle == 180:
        newPos[1] -= distance
    elif moveAngle == 270:
        newPos[0] -= distance
    return newPos

def changeAngle(oldAngle, turnAngle):
    newAngle = (oldAngle + turnAngle)%360
    if newAngle < 0:
        newAngle -= 360
    return newAngle

for x in instructions:
    instruction = [x[0], int(x[1:])]

    if instruction[0] == "N":
        position[1] += instruction[1]
    elif instruction[0] == "S":
        position[1] -= instruction[1]
    elif instruction[0] == "E":
        position[0] += instruction[1]
    elif instruction[0] == "W":
        position[0] -= instruction[1]
    elif instruction[0] == "L":
        angle = changeAngle(angle, -instruction[1])
    elif instruction[0] == "R":
        angle = changeAngle(angle, instruction[1])
    elif instruction[0] == "F":
        position = move(position, angle, instruction[1])

manhattanDist = abs(position[0]) + abs(position[1])
print(manhattanDist)