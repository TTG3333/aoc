with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

rules = {x:[] for x in range(10,100)}
books = []
for i, line in enumerate(lines):
    if line == "":
        books = lines[i+1:]
        break
    first, second = [int(x) for x in line.split("|")]
    rules[second].append(first)

def checkSequence(nums):
    illegals = set()
    seen = set()
    for num in nums:
        if num in illegals:
            return False
        seen.add(num)
        for check in rules[num]:
            if check not in seen:
                illegals.add(check)
    return True

total = 0
for book in books:
    nums = [int(x) for x in book.split(",")]
    if checkSequence(nums):
        total += nums[len(nums)//2]
print(total)