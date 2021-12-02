with open("Input.txt", "tr") as F:
    nums = [int(x) for x in F.read().splitlines()]
unique_nums = {}
for y, x in enumerate(nums):
    if x not in unique_nums:
        unique_nums[x] = {0: y, 1: None}
    else:
        unique_nums[x][0], unique_nums[x][1] = y, unique_nums[x][0]
spoken = list(nums)
for x in range(len(nums), 30000000):
    lngth = len(spoken)
    last = spoken[x-1]
    if unique_nums[last][1] != None:
        lastIndex = unique_nums[last][0]
        secondLastIndex = unique_nums[last][1]
        num = lastIndex-secondLastIndex
        try:
            unique_nums[num][0], unique_nums[num][1] = x, unique_nums[num][0]
        except KeyError:
            unique_nums[num] = {0: x, 1: None}
        spoken.append(num)
    else:
        num = 0
        try:
            unique_nums[num][0], unique_nums[num][1] = x, unique_nums[num][0]
        except KeyError:
            unique_nums[num] = {0: x, 1: None}
        spoken.append(0)
print(spoken[-1])