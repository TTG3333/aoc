with open("Input.txt", "tr") as F:
    bins = F.read().splitlines()

def returnNums(nums, bit, comp):
    sortedNums = [[], []]
    for x in nums:
        if x[bit] == "0":
            sortedNums[0].append(x)
        else:
            sortedNums[1].append(x)
    if comp:
        return sortedNums[0] if len(sortedNums[0]) > len(sortedNums[1]) else sortedNums[1]
    else:
        return sortedNums[1] if len(sortedNums[0]) > len(sortedNums[1]) else sortedNums[0]

nums = list(bins)
for x in range(len(bins[0])):
    nums = returnNums(nums, x, True)
    if len(nums) == 1:
        break
oxygen = int(nums[0], base=2)
nums = list(bins)
for x in range(len(bins[0])):
    nums = returnNums(nums, x, False)
    if len(nums) == 1:
        break
co2 = int(nums[0], base=2)
print(oxygen*co2)