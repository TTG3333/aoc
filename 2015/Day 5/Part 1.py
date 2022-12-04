with open("Input.txt", "tr") as F:
    strings = F.read().splitlines()
vowels = "aeiou"
badStrings = ["ab", "cd", "pq", "xy"]

count = 0
for s in strings:
    doubleBreak = False
    for badS in badStrings:
        if badS in s:
            doubleBreak = True
            break
    if doubleBreak:
        continue
    vowelCount = sum([s.count(x) for x in vowels])
    if vowelCount < 3:
        continue
    for i, letter in enumerate(s[:-1]):
        if s[i+1] == letter:
            break
    else:
        continue
    count += 1
print(count)