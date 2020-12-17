with open("Input.txt", "tr") as F:
    lines = F.read().split("\n")
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
    correct_passports = 0
    for x in refined_passports:
        for y in strs_to_check:
            if x.count(y) != 1:
                break
        else:
            correct_passports += 1
    print(correct_passports)
    F.close()