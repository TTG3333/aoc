with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

def checkResult(result, current, nums):
    if len(nums) == 1:
        return current + nums[0] == result or current * nums[0] == result
    return checkResult(result, current + nums[0], nums[1:]) or checkResult(result, current * nums[0], nums[1:])

total = 0
for line in lines:
    result, nums = line.split(": ")
    result = int(result)
    nums = [int(x) for x in nums.split(" ")]
    total += result * checkResult(result, nums[0], nums[1:])
print(total)