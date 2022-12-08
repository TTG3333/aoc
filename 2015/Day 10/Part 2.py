with open("Input.txt", "tr") as F:
    nums = F.read()

def lookSay(nums):
    newNums = ""
    current = nums[0]
    count = 1
    for char in nums[1:]:
        if char == current:
            count += 1
        else:
            newNums += str(count) + current
            current = char
            count = 1
    newNums += str(count) + current
    return newNums

for _ in range(50):
    nums = lookSay(nums)
print(len(nums))