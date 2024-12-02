with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

def checkNums(nums):
    increasing = None
    if nums[1] > nums[0]:
        increasing = True
    elif nums[0] > nums[1]:
        increasing = False
    else:
        return False

    for y, num in enumerate(nums[:-1]):
        if increasing and (num > nums[y+1] or abs(num - nums[y+1]) not in [1, 2, 3]):
            break
        elif not increasing and (num < nums[y+1] or abs(num - nums[y+1]) not in [1, 2, 3]):
            break
    else:
        return True
    return False

safe = 0
for line in lines:
    nums = [int(x) for x in line.split(" ")]
    removed = False
    if checkNums(nums):
        safe += 1
    else:
        for i in range(len(nums)):
            if i < len(nums)-1:
                if checkNums(nums[:i]+nums[i+1:]):
                    break
            else:
                if checkNums(nums[:-1]):
                    break
        else:
            continue
        safe += 1

print(safe)