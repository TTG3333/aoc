with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
pairs = {"[": "]", "(": ")", "{": "}", "<": ">"}
rewards = {")": 1, "]": 2, "}": 3, ">": 4}

scores = []
for line in lines:
    score = 0
    openingChars = []
    for char in line:
        if char in list(pairs.keys()):
            openingChars.append(char)
        elif char == pairs[openingChars[-1]]:
            openingChars.pop()
        else:
            break
    else:
        for char in openingChars[::-1]:
            score *= 5
            score += rewards[pairs[char]]
        scores.append(score)
scores.sort()
print(scores[len(scores)//2])