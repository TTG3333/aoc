with open("Input.txt", "tr") as F:
    insts = F.read().splitlines()

dirs = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
visited = {(0, 0)}
positions = [[0, 0] for _ in range(10)]
for inst in insts:
    dir, val = inst.split(" ")
    val = int(val)
    for _ in range(val):
        positions[0][0] += dirs[dir][0]
        positions[0][1] += dirs[dir][1]
        for knot in range(1, 10):
            headPos = positions[knot-1]
            tailPos = positions[knot]
            for k in range(2):
                if headPos[0 + k] - tailPos[0 + k] > 1:
                    if headPos[1 - k] - tailPos[1 - k] >= 1:
                        tailPos[1 - k] += 1
                    elif headPos[1 - k] - tailPos[1 - k] <= -1:
                        tailPos[1 - k] -= 1
                    tailPos[0 + k] += 1
                elif headPos[0 + k] - tailPos[0 + k] < -1:
                    if headPos[1 - k] - tailPos[1 - k] >= 1:
                        tailPos[1 - k] += 1
                    elif headPos[1 - k] - tailPos[1 - k] <= -1:
                        tailPos[1 - k] -= 1
                    tailPos[0 + k] -= 1
        visited.add(tuple(positions[-1]))
print(len(visited))