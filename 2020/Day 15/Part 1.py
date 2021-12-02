with open("Input.txt", "tr") as F:
    nums = [int(x) for x in F.read().splitlines()]
spoken = list(nums)
for x in range(len(nums), 2020):
    if spoken.count(spoken[x-1]) == 1:
        spoken.append(0)
    else:
        lastIndex = len(spoken)-spoken[::-1].index(spoken[x-1])-1
        upToLast = spoken[:lastIndex]
        secondLastIndex = len(upToLast)-upToLast[::-1].index(spoken[x-1])-1
        spoken.append(lastIndex-secondLastIndex)
print(spoken[-1])