with open("Input.txt", "tr") as F:
    data = [[int(y) for y in x.split("..")] for x in F.read()[15:].split(", y=")]
y = -data[1][0] - 1
maxY = (y**2+y)//2
print(maxY)