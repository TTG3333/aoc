with open("Input.txt", "tr") as F:
    inst = F.read().splitlines()

instructions = [x.split(" = ") for x in inst]

def findValsFromFloat(xList, binNum, vals):
    for x in range(2):
        newBin = binNum[:xList[0]] + str(x) + binNum[xList[0]+1:]
        if len(xList) == 1:
            vals.append(int("0b"+newBin, 2))
        else:
            vals = findValsFromFloat(xList[1:], newBin, vals)
    return vals

mem = {}
mask = ""
for x in instructions:
    if x[0] == "mask":
        mask = x[1]
    else:
        address = x[0][4:-1]
        shortBinVal = bin(int(address))[2:]
        binVal = "0"*(36-len(shortBinVal))+shortBinVal
        finalBin = ""
        xList = []
        for y, z in enumerate(mask):
            if z == "X":
                xList.append(y)
                finalBin += z
            elif z == "1":
                finalBin += z
            else:
                finalBin += binVal[y]
        addresses = findValsFromFloat(xList, finalBin, [])
        for z in addresses:
            mem[z] = int(x[1])

sum = 0
for value in mem.values():
    sum += value
print(sum)