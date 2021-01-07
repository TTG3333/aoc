with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
ids = []
for x in lines:
    row = [0, 127]
    column = [0, 7]
    for y in x[:6]:
        if y == "B":
            row[0] = row[0]+round((row[1]-row[0])/2)
        elif y == "F":
            row[1] = row[0]+(row[1]-row[0])//2
    if x[6] == "B":
        row = row[1]
    elif x[6] == "F":
        row = row[0]
    for y in x[7:-1]:
        if y == "L":
            column[1] = column[0]+(column[1]-column[0])//2
        elif y == "R":
            column[0] = column[0]+round((column[1]-column[0])/2)
    if x[-1] == "L":
        column = column[0]
    elif x[-1] == "R":
        column = column[1]
    
    id = row * 8 + column
    ids.append(id)

ids.sort()
last_id = 0
for y, x in enumerate(ids):
    if x == last_id + 2:
        print(x-1)
    last_id = x