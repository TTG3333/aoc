with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

rules = {x:set() for x in range(10,100)} # the value is all the pages that must come before the key
books = []
for i, line in enumerate(lines):
    if line == "":
        books = lines[i+1:]
        break
    first, second = [int(x) for x in line.split("|")]
    rules[second].add(first)

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

def propagateRules(num, rules, visited): # propagates the rules so that dependencies of dependencies are reflected in the parent's value
    visited.add(num)
    returned = set()
    for k in rules[num]:
        if k not in visited:
            returned |= propagateRules(k, rules, visited)
    return rules[num]|returned

total = 0
for book in books:
    nums = [int(x) for x in book.split(",")]
    if not checkSequence(nums):
        newRules = {key:{x for x in value if x in nums} for key, value in rules.items() if key in nums} # Only take keys and values in this book
        for num in newRules:
            newRules[num] = propagateRules(num, newRules, set())
        nums = sorted(nums, key=lambda a: len(newRules[a]))
        total += nums[len(nums)//2]
print(total)