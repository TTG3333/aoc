def count_trees(values, xIncrement, yIncrement):
    pos = {
        "x": -xIncrement,
        "y": -yIncrement
    }
    trees = 0
    for x in range(len(values)//yIncrement):
        pos["x"] += xIncrement
        pos["y"] += yIncrement
        if values[pos["y"]][pos["x"]%len(values[pos["y"]])] == "#":
            trees += 1
    return trees

with open("Input.txt", "tr") as F:
    lines = F.read().split("\n")
    checks = [
        {
            "x": 1,
            "y": 1
        },
        {
            "x": 3,
            "y": 1
        },
        {
            "x": 5,
            "y": 1
        },
        {
            "x": 7,
            "y": 1
        },
        {
            "x": 1,
            "y": 2
        }
    ]

    total = 1
    for x in checks:
        total *= count_trees(lines, x["x"], x["y"])

    print(total)
    F.close()