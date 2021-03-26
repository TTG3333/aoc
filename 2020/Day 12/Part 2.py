with open("Input.txt", "tr") as F:
    instructions = F.read().splitlines()

position = [0, 0]
waypointPosition = [10, 1]

def move(pos, waypointPos, repetitions):
    newPos = pos
    newPos[0] += waypointPos[0] * repetitions
    newPos[1] += waypointPos[1] * repetitions
    return newPos

def turnWaypoint(waypointPos, turnAngle):
    newPos = [0, 0]
    angle = turnAngle%360
    if angle < 0:
        angle -= 360
    if angle == 90:
        newPos[0] = waypointPos[1]
        newPos[1] = -waypointPos[0]
    elif angle == 180:
        newPos[0] = -waypointPos[0]
        newPos[1] = -waypointPos[1]
    elif angle == 270:
        newPos[0] = -waypointPos[1]
        newPos[1] = waypointPos[0]
    return newPos

for x in instructions:
    instruction = [x[0], int(x[1:])]

    if instruction[0] == "N":
        waypointPosition[1] += instruction[1]
    elif instruction[0] == "S":
        waypointPosition[1] -= instruction[1]
    elif instruction[0] == "E":
        waypointPosition[0] += instruction[1]
    elif instruction[0] == "W":
        waypointPosition[0] -= instruction[1]
    elif instruction[0] == "L":
        waypointPosition = turnWaypoint(waypointPosition, -instruction[1])
    elif instruction[0] == "R":
        waypointPosition = turnWaypoint(waypointPosition, instruction[1])
    elif instruction[0] == "F":
        position = move(position, waypointPosition, instruction[1])
    print(instruction, waypointPosition, position)

manhattanDist = abs(position[0]) + abs(position[1])
print(manhattanDist)