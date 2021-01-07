with open("Input.txt", "tr") as F:
    numbers = F.read().splitlines()
fixed_numbers = []
for y, x in enumerate(numbers):
    fixed_numbers.append(int(x))
answer = 0
for index, x in enumerate(fixed_numbers[25:], 25):
    for y in fixed_numbers[index-25:index]:
        for z in fixed_numbers[index-25:index]:
            if y == z:
                continue
            if y + z == x:
                break
        else:
            continue
        break
    else:
        answer = x
        break
print(answer)