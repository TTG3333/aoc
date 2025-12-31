import re

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

*nums, operators = lines

for i, line in enumerate(nums):
    nums[i] = [int(x) for x in re.sub(r"\s+", " ", line).strip().split(" ")]
operators = re.sub(r"\s+", " ", operators).strip().split(" ")

total = 0
for i in range(len(operators)):
    if operators[i] == "+":
        res = 0
        for k in range(len(nums)):
            res += nums[k][i]
    elif operators[i] == "*":
        res = 1
        for k in range(len(nums)):
            res *= nums[k][i]
    total += res
print(total)