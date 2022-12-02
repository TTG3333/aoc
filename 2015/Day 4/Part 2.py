from hashlib import md5

with open("Input.txt", "tr") as F:
    key = F.read()
i = 1
while True:
    hashval = md5(bytes(key+str(i), encoding="ascii")).hexdigest()
    if hashval.startswith("000000"):
        break
    i += 1
print(i)