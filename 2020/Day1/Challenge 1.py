F = open("Input.txt", "tr")
numbers = F.read().split("\n")
F.close()

for x in numbers:
    xNum = int(x)
    num = 2020 - xNum
    for y in numbers:
        yNum = int(y)
        if num == yNum:
            print(yNum*xNum)