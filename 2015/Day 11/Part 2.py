from string import ascii_lowercase

with open("Input.txt", "tr") as F:
    inp = F.read()

letters = [x for x in ascii_lowercase]
letters.remove("i")
letters.remove("o")
letters.remove("l")
totalLetters = len(letters)
l2n = {letters[i]: i for i in range(len(letters))}
n2l = {v: k for k, v in l2n.items()}
pwd = [l2n[x] for x in inp[::-1]]

while True:
    pwd[0] += 1
    for i, val in enumerate(pwd):
        if val >= totalLetters:
            pwd[i] = 0
            pwd[i+1] += 1
    pwdS = "".join([n2l[x] for x in pwd[::-1]])
    for i in range(len(ascii_lowercase) - 2):
        if ascii_lowercase[i:i+3] in pwdS:
            break
    else:
        continue
    for i, letter in enumerate(pwdS[:-1]):
        if pwdS[i+1] == letter:
            break
    else:
        continue
    for k, letter in enumerate(pwdS[i+2:-1], start = i+2):
        if pwdS[k+1] == letter:
            break
    else:
        continue
    break
print(pwdS)