with open("Input.txt", "tr") as F:
    numbers = F.read().splitlines()
for x in numbers:
    xNum = int(x)
    for y in numbers:
        yNum = int(y)
        for z in numbers:
            zNum = int(z)
            if xNum + yNum + zNum == 2020:
                print(xNum*yNum*zNum)