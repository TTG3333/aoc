with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

mCount = 0
monkeys = {}
for line in lines:
    if line.startswith("Monkey"):
        mCount = int(line.split(" ")[1][:-1])
        continue
    elif line.startswith("  Starting"):
        monkeys[mCount] = {"items": [int(x) for x in line[18:].split(", ")], "inspections": 0}
    elif line.startswith("  Operation"):
        line = line[19:]
        if line == "old * old":
            fct = lambda a, b: a**b
            val = 2
        else:
            line = line.split(" ")
            val = int(line[2])
            if line[1] == "*":
                fct = lambda a, b: a * b
            elif line[1] == "+":
                fct = lambda a, b: a + b
        monkeys[mCount]["val"] = val
        monkeys[mCount]["fct"] = fct
    elif line.startswith("  Test"):
        monkeys[mCount]["test"] = int(line.split(" ")[-1])
    elif line.startswith("    If true"):
        monkeys[mCount][True] = int(line.split(" ")[-1])
    elif line.startswith("    If false"):
        monkeys[mCount][False] = int(line.split(" ")[-1])

for _ in range(20):
    for m in range(len(monkeys)):
        monkey = monkeys[m]
        for item in monkey["items"]:
            monkey["inspections"] += 1
            item = monkey["fct"](item, monkey["val"])//3
            monkeys[monkey[item%monkey["test"]==0]]["items"].append(item)
        monkey["items"] = []

sortedMonkeys = sorted(monkeys.values(), key = lambda a: a["inspections"], reverse=True)
print(sortedMonkeys[0]["inspections"]*sortedMonkeys[1]["inspections"])