with open("Input.txt", "tr") as F:
    insts = F.read().splitlines()

dirs = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
visited = {(0, 0)}
headPos, tailPos = [0, 0], [0, 0]
for inst in insts:
    dir, val = inst.split(" ")
    val = int(val)
    for _ in range(val):
        headPos[0] += dirs[dir][0]
        headPos[1] += dirs[dir][1]
        for k in range(2):
            if headPos[0 + k] - tailPos[0 + k] > 1:
                tailPos[1 - k] = headPos[1 - k]
                tailPos[0 + k] = headPos[0 + k] - 1
            elif headPos[0 + k] - tailPos[0 + k] < -1:
                tailPos[1 - k] = headPos[1 - k]
                tailPos[0 + k] = headPos[0 + k] + 1
        visited.add(tuple(tailPos))
print(len(visited))