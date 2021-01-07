def checkBag(bags, bag):
    amount_that_contains = 0
    if bags[bag] == None:
        return amount_that_contains
    for x in bags[bag]:
        amount_that_contains += (x["amount"] * (checkBag(bags, x["bag"]) + 1))
    return amount_that_contains

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
bags = []
for x in lines:
    bags.append(x.split(" bags")[0])
contents = []
for x in lines:
    bag_contents = x.split(" bags contain ")[1].split(", ")
    bag_contents[-1] = bag_contents[-1][:-1]
    if bag_contents == ["no other bags"]:
        bag_contents = []
        contents.append(bag_contents)
        continue
    for y, z in enumerate(bag_contents):
        bag_contents[y] = {
            "amount": int(z.split(" ")[0]),
            "bag": " ".join(z.split(" ")[1:-1])
        }
    contents.append(bag_contents)
bags_and_contents = {}
for y, x in enumerate(bags):
    if contents[y] == []:
        bags_and_contents[x] = None
        continue
    bags_and_contents[x] = contents[y]
bag_to_search = "shiny gold"
solution = checkBag(bags_and_contents, bag_to_search)
print(solution)