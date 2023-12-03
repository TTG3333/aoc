from string import digits

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

around = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def product(*args):
    total = 1
    for item in args:
        total *= item
    return total

gear_nums = {}
for i, line in enumerate(lines):
    num_str = ""
    part = False
    potential_gears = set()
    for j, char in enumerate(line):
        if char in digits:
            num_str += char
            for xOff, yOff in around:
                newX = j + xOff
                newY = i + yOff
                if newX >= 0 and newX < len(line) and newY >= 0 and newY < len(lines):
                    if lines[newY][newX] != "." and lines [newY][newX] not in digits:
                        part = True
                    if lines[newY][newX] == "*":
                        potential_gears.add((newX, newY))
        elif num_str != "":
            if part:
                for gear in potential_gears:
                    if gear in gear_nums:
                        gear_nums[gear].append(int(num_str))
                    else:
                        gear_nums[gear] = [int(num_str)]
            potential_gears = set()
            part = False
            num_str = ""
    if num_str != "":
        if part:
            for gear in potential_gears:
                if gear in gear_nums:
                    gear_nums[gear].append(int(num_str))
                else:
                    gear_nums[gear] = [int(num_str)]
        potential_gears = set()
        part = False
        num_str = ""
total = 0
for gear, vals in gear_nums.items():
    if len(vals) >= 2:
        total += product(*vals)
print(total)