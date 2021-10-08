with open("Input.txt", "tr") as F:
    inst = F.read().splitlines()

instructions = [x.split(" = ") for x in inst]

mem = {}
mask = ""
for x in instructions:
    if x[0] == "mask":
        mask = x[1]
    else:
        address = x[0][4:-1]
        shortBinVal = bin(int(x[1]))[2:]
        binVal = "0"*(36-len(shortBinVal))+shortBinVal
        finalBin = ""
        for y, z in enumerate(mask):
            if z == "X":
                finalBin += binVal[y]
            else:
                finalBin += z
        mem[address] = int("0b"+finalBin, 2)

sum = 0
for value in mem.values():
    sum += value
print(sum)