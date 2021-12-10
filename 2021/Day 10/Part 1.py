with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
pairs = {"[": "]", "(": ")", "{": "}", "<": ">"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

counter = 0
for line in lines:
    openingChars = []
    for char in line:
        if char in list(pairs.keys()):
            openingChars.append(char)
        elif char == pairs[openingChars[-1]]:
            openingChars.pop()
        else:
            counter += scores[char]
            break
print(counter)