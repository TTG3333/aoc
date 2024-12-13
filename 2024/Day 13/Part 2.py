import re
from math import ceil, gcd

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

machines = []
currentMachine = {}
for i, line in enumerate(lines):
    match i%4:
        case 0:
            currentMachine["A"] = tuple(int(x) for x in re.match(r"^Button A: X\+(\d+), Y\+(\d+)$", line).groups())
        case 1:
            currentMachine["B"] = tuple(int(x) for x in re.match(r"^Button B: X\+(\d+), Y\+(\d+)$", line).groups())
        case 2:
            currentMachine["prize"] = tuple(int(x)+10000000000000 for x in re.match(r"^Prize: X=(\d+), Y=(\d+)$", line).groups())
        case 3:
            machines.append(currentMachine)
            currentMachine = {}
machines.append(currentMachine)

def euclid(a, b): # Assume a > b, and both are non-zero
    r = [a, b]
    s = [1, 0]
    t = [0, 1]
    i = 1
    while r[i] != 0:
        quotient = r[i-1]//r[i]
        r.append(r[i-1]-quotient*r[i])
        s.append(s[i-1]-quotient*s[i])
        t.append(t[i-1]-quotient*t[i])
        i += 1
    return (s[i-1], t[i-1])

def solveMachine(machine):
    xA, yA = machine["A"]
    xB, yB = machine["B"]
    prizeX, prizeY = machine["prize"]
    divisorX = gcd(xA, xB)
    divisorY = gcd(yA, yB)
    if prizeX%divisorX != 0 or prizeY%divisorY != 0:
        return 0
    xA, xB, prizeX = xA//divisorX, xB//divisorX, prizeX//divisorX
    yA, yB, prizeY = yA//divisorY, yB//divisorY, prizeY//divisorY
    euclidX = euclid(xA, xB) # The equation is prizeX = a*xA + b*xB, the solution is a = aCoefX*k+aOffsetX, b = bCoefX*k+bOffsetX, k an integer
    aCoefX = xB
    aOffsetX = euclidX[0] * prizeX
    bCoefX = -xA
    bOffsetX = euclidX[1] * prizeX
    aCoefY = yA*aCoefX # Plug the values for a and b into the equation for prizeY and check that it holds
    aOffsetY = yA*aOffsetX
    bCoefY = yB*bCoefX
    bOffsetY = yB*bOffsetX
    match aCoefY + bCoefY: # This value will be the resulting coefficient for k
        case 0: # The k cancels out in the equation for b, so the offsets must equal the prizeY
            if prizeY != aOffsetY+bOffsetY:
                return 0
            else: # All values for k are valid, need to find the one with the smallest cost
                kCoef = 3*aCoefX + bCoefX # price = k*kCoef + kOffset
                kOffset = 3*aOffsetX + bOffsetX
                k = ceil(-kOffset/kCoef)
                return 3*(aCoefX*k+aOffsetX) + bCoefX*k+bOffsetX
        case coef: # values for k don't cancel out, so only one valid solution
            k = (prizeY-(aOffsetY+bOffsetY))/coef
            if k % 1 != 0:
                return 0
            return 3*(aCoefX*k+aOffsetX) + bCoefX*k+bOffsetX

total = 0
for machine in machines:
    total += solveMachine(machine)
print(total)