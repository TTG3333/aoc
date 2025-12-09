with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

total = 0
for line in lines:
    nums = [int(x) for x in line]
    first = 0
    if nums[0] != 9:
        for i, n in enumerate(nums[1:-1], start=1):
            if n > nums[first]:
                first = i
                if n == 9:
                    break
    second = nums[first + 1]
    if first < len(nums) - 2:
        for n in nums[first + 2:]:
            if n > second:
                second = n
                if n == 9:
                    break
    total += 10*nums[first] + second
print(total)