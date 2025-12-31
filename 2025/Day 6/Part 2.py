def product(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

*nums, operators = lines
nums = nums[::-1] # Have the least significant digit line on top

operators_positions = [i for i, c in enumerate(operators) if c != " "] + [len(operators)+1]

total = 0
current = operators_positions[0]
for following in operators_positions[1:]:
    operator = operators[current]
    current_numbers = []
    for pos in range(following-2, current-1, -1):
        n = 0
        k_offset = 0
        for k in range(len(nums)):
            val = nums[k][pos]
            if val == " ":
                k_offset -= 1
                continue
            n += 10**(k+k_offset) * (int(nums[k][pos]) if nums[k][pos] != " " else 0)
        current_numbers.append(n)
    if operator == "+":
        total += sum(current_numbers)
    elif operator == "*":
        total += product(current_numbers)
    current = following
print(total)