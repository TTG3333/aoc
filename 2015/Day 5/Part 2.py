with open("Input.txt", "tr") as F:
    strings = F.read().splitlines()

count = 0
for s in strings:
    pairs = {} # Value is the index of the first occurrence
    cond1 = cond2 = False
    for i, letter in enumerate(s[:-1]):
        if not cond1:
            pair = s[i:i+2]
            if pair in pairs:
                if pairs[pair] < i-1:
                    cond1 = True
            else:
                pairs[pair] = i
        if not cond2 and i < len(s)-2:
            if s[i+2] == letter:
                cond2 = True
        if cond1 and cond2:
            count += 1
            break
print(count)