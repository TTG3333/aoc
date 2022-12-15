with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

def constrain(val, small, big):
    if val < small:
        return small
    elif val > big:
        return big
    return val

stopVal = 2503
reindeer = []
for line in lines:
    line = line.split(" ")
    dist = int(line[3])
    time = int(line[6])
    rest = int(line[-2])
    val = 0
    val += (stopVal//(time+rest))*(dist*time)
    rem = stopVal%(time+rest)
    val += constrain(rem, 0, time)*dist
    reindeer.append(val)
print(max(reindeer))