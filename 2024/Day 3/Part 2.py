from string import digits

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

total = 0
test = "mul("
do = "do()"
dont = "don't()"
enabled = True
for line in lines:
    temp = 0 # Index in test, 4 is , and 5 is )
    doTemp = dontTemp = 0
    num1 = ""
    num2 = ""
    for char in line:
        if enabled:
            if temp < 4:
                if char == test[temp]:
                    temp += 1
                else:
                    num1 = num2 = ""
                    temp = 0
            elif temp == 4:
                if char == ',':
                    if len(num1) == 0:
                        num1 = num2 = ""
                        temp = 0
                    else:
                        temp = 5
                elif char in digits:
                    num1 += char
                else:
                    num1 = num2 = ""
                    temp = 0
            elif temp == 5:
                if char == ')':
                    if len(num2) == 0:
                        num1 = num2 = ""
                        temp = 0
                    else:
                        total += int(num1) * int(num2)
                        num1 = num2 = ""
                        temp = 0
                elif char in digits:
                    num2 += char
                else:
                    num1 = num2 = ""
                    temp = 0
        if char == do[doTemp]:
            doTemp += 1
        else:
            doTemp = 0
        if char == dont[dontTemp]:
            dontTemp += 1
        else:
            dontTemp = 0
        if doTemp == len(do):
            enabled = True
            num1 = num2 = ""
            temp = doTemp = dontTemp = 0
        if dontTemp == len(dont):
            enabled = False
            num1 = num2 = ""
            temp = doTemp = dontTemp = 0

print(total)