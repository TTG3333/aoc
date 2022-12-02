with open("Input.txt", "tr") as F:
    presents = F.read().splitlines()
ribbon = 0
for present in presents:
    l, w, h = [int(x) for x in present.split("x")]
    if l == max(l, w, h):
        ribbon += l*w*h + 2*(w+h)
    elif w == max(l, w, h):
        ribbon += l*w*h + 2*(l+h)
    elif h == max(l, w, h):
        ribbon += l*w*h + 2*(w+l)
print(ribbon)