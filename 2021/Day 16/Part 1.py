with open("Input.txt", "tr") as F:
    data = F.read()
for y, x in enumerate(data):
    if x != "0":
        data = "0000"*y + bin(int(data[y:], base=16))[2:]
        break
while len(data)%4 != 0:
    data = "0" + data
index = 0

def decode():
    global index
    ver = int(data[index:index+3], base=2)
    if int(data[index+3:index+6], base=2) == 4:
        count = 0
        while True:
            if data[index+6+5*count] == "0":
                break
            count += 1
        index += 6+5*(count+1)
    else:
        if data[index+6] == "0":
            count = int(data[index+7:index+22], base=2)
            start = index+22
            index += 22
            while index < count+start:
                ver += decode()
        else:
            count = int(data[index+7:index+18], base=2)
            index += 18
            for _ in range(count):
                ver += decode()
    return ver

print(decode())