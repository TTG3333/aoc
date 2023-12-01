from string import digits
digits_str = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
digits_str_back = {chars[::-1]:val for chars, val in digits_str.items()}

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
total = 0
for line in lines:
    for i, char in enumerate(line):
        if char in digits:
            smallest_num = None
            for num in digits_str:
                index = line.find(num)
                if index != -1 and index < i:
                    i = index
                    smallest_num = num
            if smallest_num == None:
                total += 10*int(char)
            else:
                total += 10*digits_str[smallest_num]
            break
    else:
        smallest_num = None
        for num in digits_str:
            index = line.find(num)
            if index != -1 and index < i:
                i = index
                smallest_num = num
        total += 10*digits_str[smallest_num]
    for i, char in enumerate(line[::-1]):
        if char in digits:
            smallest_num = None
            for num in digits_str_back:
                index = line[::-1].find(num)
                if index != -1 and index < i:
                    i = index
                    smallest_num = num
            if smallest_num == None:
                total += int(char)
            else:
                total += digits_str_back[smallest_num]
            break
    else:
        smallest_num = None
        for num in digits_str_back:
            index = line[::-1].find(num)
            if index != -1 and index < i:
                i = index
                smallest_num = num
        total += digits_str_back[smallest_num]
print(total)