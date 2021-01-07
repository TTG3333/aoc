def checkBags(bags, bag):
    bags_that_can_contain = []
    for key, value in bags.items():
        if value == None:
            continue
        for x in value:
            if x == bag:
                bags_that_can_contain.append(key)
                for y in checkBags(bags, key):
                    bags_that_can_contain.append(y)
                break
    return bags_that_can_contain

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
bags = []
for x in lines:
    bags.append(x.split(" bags")[0])
contents = []
for x in lines:
    bag_contents = x.split(" bags contain ")[1].split(", ")
    bag_contents[-1] = bag_contents[-1][:-1]
    for y, z in enumerate(bag_contents):
        bag_contents[y] = " ".join(z.split(" ")[1:-1])
    if bag_contents[0] == "other":
        bag_contents = []
    contents.append(bag_contents)
bags_and_contents = {}
for y, x in enumerate(bags):
    if contents[y] == []:
        bags_and_contents[x] = None
        continue
    bags_and_contents[x] = contents[y]
bag_to_find = "shiny gold"
solutions = checkBags(bags_and_contents, bag_to_find)
different_solutions = []
for x in solutions:
    if different_solutions == []:
        different_solutions.append(x)
        continue
    for y in different_solutions:
        if y == x:
            break
    else:
        different_solutions.append(x)
print(len(different_solutions))