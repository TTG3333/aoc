with open("Input.txt", "tr") as F:
    passwords = F.read().split("\n")
    pwd = []
    for y, x in enumerate(passwords):
        pwd.append(x.split(" "))
        pwd[y][0] = pwd[y][0].split("-")
        pwd[y][1] = pwd[y][1].strip(":")
    correct_pwd = 0
    for x in pwd:
        correct_ltr = 0
        for y in x[0]:
            if x[2][int(y)-1] == x[1]:
                correct_ltr += 1
        if correct_ltr == 1:
            correct_pwd += 1
    print(correct_pwd)    
    F.close()