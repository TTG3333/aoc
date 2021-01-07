with open("Input.txt", "tr") as F:
    numbers = F.read().splitlines()
fixed_numbers = []
for y, x in enumerate(numbers):
    fixed_numbers.append(int(x))
invalid_number = 0
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
        invalid_number = x
        break
tested_numbers = []
for y, x in enumerate(fixed_numbers):
    tested_numbers = [x]
    sum = x
    if y >= len(fixed_numbers)-1:
        continue
    for z in fixed_numbers[y+1:]:
        tested_numbers.append(z)
        sum += z
        if sum >= invalid_number:
            break
    else:
        continue
    if sum == invalid_number:
        break
tested_numbers.sort()
answer = tested_numbers[0] + tested_numbers[-1]
print(answer)