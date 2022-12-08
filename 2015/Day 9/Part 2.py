with open("Input.txt", "tr") as F:
    dists = F.read().splitlines()

cities = {}
for dist in dists:
    orig, dest, d = dist.split(" ")[::2]
    d = int(d)
    if orig not in cities:
        cities[orig] = {}
    if dest not in cities:
        cities[dest] = {}
    cities[orig][dest] = d
    cities[dest][orig] = d

def checkCities(city, cities, citiesToGo):
    dists = []
    for c in citiesToGo:
        newCTG = citiesToGo.copy()
        newCTG.remove(c)
        if len(newCTG) != 0:
            dists.append(checkCities(c, cities, newCTG) + cities[city][c])
        else:
            dists.append(cities[city][c])
    return max(dists)

shortest = float("-inf")
for city in cities.keys():
    val = checkCities(city, cities, list(cities[city].keys()))
    if val > shortest:
        shortest = val
print(shortest)