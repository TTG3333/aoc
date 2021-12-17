with open("Input.txt", "tr") as F:
    data = F.read()
for y, x in enumerate(data):
    if x != "0":
        data = "0000"*y + bin(int(data[y:], base=16))[2:]
        break
while len(data)%4 != 0:
    data = "0" + data
index = 0

def product(lst):
    val = 1
    for x in lst:
        val *= x
    return val

def decode():
    global index
    val = 0
    packType = int(data[index+3:index+6], base=2)
    if packType == 4:
        count = 0
        binVals = ""
        while True:
            binVals += data[index+7+5*count:index+11+5*count]
            if data[index+6+5*count] == "0":
                break
            count += 1
        index += 6+5*(count+1)
        val += int(binVals, base=2)
    else:
        returns = []
        if data[index+6] == "0":
            count = int(data[index+7:index+22], base=2)
            start = index+22
            index += 22
            while index < count+start:
                returns.append(decode())
        else:
            count = int(data[index+7:index+18], base=2)
            index += 18
            for _ in range(count):
                returns.append(decode())
        if packType == 0:
            val += sum(returns)
        elif packType == 1:
            val += product(returns)
        elif packType == 2:
            val += min(returns)
        elif packType == 3:
            val += max(returns)
        elif packType == 5:
            val += 1 if returns[0] > returns[1] else 0
        elif packType == 6:
            val += 1 if returns[0] < returns[1] else 0
        elif packType == 7:
            val += 1 if returns[0] == returns[1] else 0
    return val

print(decode())