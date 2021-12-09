from string import ascii_lowercase

with open("Input.txt", "tr") as F:
    nums = [[[z for z in y.split(" ")] for y in x.split(" | ")] for x in F.read().splitlines()]

numbers = {
    0: ["a", "b", "c", "e", "f", "g"],
    1: ["c", "f"],
    2: ["a", "c", "d", "e", "g"],
    3: ["a", "c", "d", "f", "g"],
    4: ["b", "c", "d", "f"],
    5: ["a", "b", "d", "f", "g"],
    6: ["a", "b", "d", "e", "f", "g"],
    7: ["a", "c", "f"],
    8: ["a", "b", "c", "d", "e", "f", "g"],
    9: ["a", "b", "c", "d", "f", "g"]}

class Digit:
    def __init__(self):
        self.layout = {x: [] for x in ascii_lowercase[:7]}
    
    def flip(self):
        self.layout2 = {value: key for key, value in self.layout.items()}
    
    def convert(self, string):
        fixedString = [self.layout2[x] for x in string]
        fixedString = "".join(sorted(fixedString))
        for number in numbers.keys():
            if "".join(numbers[number]) == fixedString:
                return number

count = 0
for num in nums:
    digit = Digit()
    patterns = num[0]
    patternsBySegCount = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for pattern in patterns:
        lngth = len(pattern)
        patternsBySegCount[lngth].append(pattern)
    digit.layout["c"].extend([x for x in patternsBySegCount[2][0]])
    digit.layout["f"].extend([x for x in patternsBySegCount[2][0]])
    for x in patternsBySegCount[3][0]:
        if x not in digit.layout["c"]:
            digit.layout["a"] = x
    for x in patternsBySegCount[4][0]:
        if x not in digit.layout["c"]:
            digit.layout["b"].append(x)
            digit.layout["d"].append(x)
    for pattern in patternsBySegCount[6]:
        counter = 0
        for x in pattern:
            if x in digit.layout["c"]:
                counter += 1
        if counter == 1:
            for y, x in enumerate(digit.layout["c"]):
                if x not in pattern:
                    digit.layout["c"] = x
                    if y == 1:
                        digit.layout["f"] = digit.layout["f"][0]
                    else:
                        digit.layout["f"] = digit.layout["f"][1]
                    break
            break
    for pattern in patternsBySegCount[5]:
        if digit.layout["c"] in pattern and digit.layout["f"] in pattern:
            for x in pattern:
                if x in digit.layout["d"]:
                    digit.layout["d"] = x
                    break
            for x in pattern:
                if x not in [digit.layout["a"], digit.layout["c"], digit.layout["d"], digit.layout["f"]]:
                    digit.layout["g"] = x
                    break
    for x in digit.layout["b"]:
        if x != digit.layout["d"]:
            digit.layout["b"] = x
    items = list(digit.layout.values())
    items.remove([])
    for letter in ascii_lowercase[:7]:
        if letter not in items:
            digit.layout["e"] = letter
    digit.flip()
    string = ""
    for number in num[1]:
        string += str(digit.convert(number))
    count += int(string)
print(count)