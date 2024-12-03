from string import digits

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

total = 0
test = "mul("
for line in lines:
    temp = 0 # Index in test, 4 is , and 5 is )
    num1 = ""
    num2 = ""
    for char in line:
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


print(total)