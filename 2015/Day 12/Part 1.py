from string import digits

with open("Input.txt", "tr") as F:
    data = F.read()

dashWDigits = digits + "-"

total = 0
inNum = False
currentNum = ""
for char in data:
    if char in dashWDigits:
        inNum = True
        currentNum += char
    elif inNum:
        inNum = False
        total += int(currentNum)
        currentNum = ""
print(total)