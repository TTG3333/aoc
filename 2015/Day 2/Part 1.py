with open("Input.txt", "tr") as F:
    presents = F.read().splitlines()
paper = 0
for present in presents:
    l, w, h = [int(x) for x in present.split("x")]
    paper += 2*(l*w+w*h+h*l) + min(l*w,w*h,h*l)
print(paper)