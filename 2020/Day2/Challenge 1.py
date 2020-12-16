with open("Input.txt", "tr") as F:
    passwords = F.read().split("\n")
    pwd = []
    for y, x in enumerate(passwords):
        pwd.append(x.split(" "))
        pwd[y][0] = pwd[y][0].split("-")
        pwd[y][1] = pwd[y][1].strip(":")
    correct_pwd = 0
    for x in pwd:
        count = x[2].count(x[1])
        if count >= int(x[0][0]) and count <= int(x[0][1]):
            correct_pwd += 1
    print(correct_pwd)    
    F.close()