with open("Input.txt", "tr") as F:
    numbers = F.read().split("\n")
    for x in numbers:
        xNum = int(x)
        num = 2020 - xNum
        for y in numbers:
            yNum = int(y)
            if num == yNum:
                print(yNum*xNum)
    F.close()