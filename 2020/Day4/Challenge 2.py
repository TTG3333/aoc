def check_colour(colour):
    if len(colour) != 7:
        return False
    
    if colour[0] != "#":
        return False
    
    for x in colour[1:]:
        chars_to_check = "0123456789abcdef"
        for y in chars_to_check:
            if x == y:
                break
        else:
            return False

def check_passport(passport):
    if not (int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002):
        return False

    if not (int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020):
        return False

    if not (int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030):
        return False

    if passport["hgt"].endswith("cm"):
        height = int(passport["hgt"].strip("cm"))
        if not (height >= 150 and height <= 193):
            return False
    elif passport["hgt"].endswith("in"):
        height = int(passport["hgt"].strip("in"))
        if not (height >= 59 and height <= 76):
            return False
    else:
        return False
    
    if check_colour(passport["hcl"]) == False:
        return False
    
    colours_to_check = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for x in colours_to_check:
        if passport["ecl"] == x:
            break
    else:
        return False
    
    if len(passport["pid"]) != 9:
        return False
    
    for x in passport["pid"]:
        nums = "0123456789"
        for y in nums:
            if x == y:
                break
        else:
            return False
    
    return True

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
refined_passports = []
passport_text = ""
for y, x in enumerate(lines):
    if y == len(lines)-1:
        refined_passports.append(x)
    else:
        if x == "":
            refined_passports.append(passport_text[:-1])
            passport_text = ""
        else:
            passport_text += (x + " ")

strs_to_check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
correct_passports = []
for x in refined_passports:
    for y in strs_to_check:
        if x.count(y) != 1:
            break
    else:
        correct_passports.append(x)

formated_passports = []
for x in correct_passports:
    to_append = {}
    for y in x.split(" "):
        to_append[y.split(":")[0]] = y.split(":")[1]
    formated_passports.append(to_append)

valid_passports = 0
for x in formated_passports:
    if check_passport(x):
        valid_passports += 1

print(valid_passports)