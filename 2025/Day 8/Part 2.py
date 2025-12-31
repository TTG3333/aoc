from math import sqrt

def product(nums):
    result = 1
    for n in nums:
        result *= n
    return result

def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

def find_representative(relationships, i):
    if relationships[i] != i:
        relationships[i] = find_representative(relationships, relationships[i])
    return relationships[i]

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

positions = [list(map(int, line.split(","))) for line in lines]
relationships = [i for i in range(len(positions))]
distances = {}
num_clusters = len(positions)

for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        dist = distance(positions[i], positions[j])
        distances[(i, j)] = dist

sorted_distances = sorted(distances.keys(), key=lambda x: distances[x])

for i, j in sorted_distances:
    if find_representative(relationships, i) != find_representative(relationships, j):
        relationships[find_representative(relationships, j)] = find_representative(relationships, i)
        num_clusters -= 1
    if num_clusters == 1:
        print(product(positions[k][0] for k in [i, j]))
        break