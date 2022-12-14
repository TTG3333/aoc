with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

people = {}
for line in lines:
    line = line[:-1].split(" ")
    first = line[0]
    second = line[-1]
    val = int(line[3]) * (-1 if line[2] == "lose" else 1)
    if first not in people:
        people[first] = {}
    people[first][second] = val

def search(score, person, toGo, people, scores, og):
    if len(toGo) == 1:
        score += people[person][toGo[0]] + people[toGo[0]][person]
        score += people[toGo[0]][og] + people[og][toGo[0]]
        scores.append(score)
    else:
        for p in toGo:
            newToGo = toGo.copy()
            newToGo.remove(p)
            search(score + people[person][p] + people[p][person], p, newToGo, people, scores, og)

scores = []
for p in people:
    toGo = list(people.keys())
    toGo.remove(p)
    search(0, p, toGo, people, scores, p)
print(max(scores))