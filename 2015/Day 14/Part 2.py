with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

stopVal = 2503
reindeer = []
for line in lines:
    line = line.split(" ")
    name = line[0]
    dist = int(line[3])
    time = int(line[6])
    rest = int(line[-2])
    reindeer.append({"dist": dist, "time": time, "rest": rest, "score": 0, "trav": 0, "tTime": time, "rTime": rest})

for _ in range(stopVal):
    for r in reindeer:
        if r["tTime"] > 1:
            r["tTime"] -= 1
            r["trav"] += r["dist"]
        elif r["tTime"] == 1:
            r["tTime"] -= 1
            r["trav"] += r["dist"]
            r["rTime"] = r["rest"]
        elif r["rTime"] == 0:
            r["tTime"] = r["time"] - 1
            r["trav"] += r["dist"]
        else:
            r["rTime"] -= 1
    max(reindeer, key = lambda a: a["trav"])["score"] += 1
print(max(reindeer, key = lambda a: a["score"])["score"])