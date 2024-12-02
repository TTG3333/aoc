with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

safe = 0
for line in lines:
    nums = [int(x) for x in line.split(" ")]
    increasing = None
    if nums[1] > nums[0]:
        increasing = True
    elif nums[0] > nums[1]:
        increasing = False
    else:
        continue

    for y, num in enumerate(nums[:-1]):
        if increasing and (num > nums[y+1] or abs(num - nums[y+1]) not in [1, 2, 3]):
            break
        elif not increasing and (num < nums[y+1] or abs(num - nums[y+1]) not in [1, 2, 3]):
            break
    else:
        safe += 1

print(safe)