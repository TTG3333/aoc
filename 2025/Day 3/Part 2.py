with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

total = 0
for line in lines:
    nums = [int(x) for x in line]
    digits = [None]*12
    pos = 0
    highest_pos = 0
    for k in range(12):
        current = nums[pos]
        highest_pos = pos
        if current == 9:
            digits[k] = 9
            pos += 1
            continue
        while pos <= len(nums) - (12 - k):
            if nums[pos] > current:
                highest_pos = pos
                current = nums[pos]
                if current == 9:
                    pos += 1
                    break
            pos += 1
        pos = highest_pos + 1
        digits[k] = current
    total += int("".join(str(x) for x in digits))
print(total)