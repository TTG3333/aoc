with open("Input.txt", "tr") as F:
    fishes = [{"age": int(x), "bd": -1} for x in F.read().split(",")]

for x in range(80):
    for y, fish in enumerate(fishes):
        if fish["bd"] >= x:
            continue
        if fish["age"] == 0:
            fishes[y]["age"] = 6
            fishes.append({"age": 8, "bd": x})
        else:
            fishes[y]["age"] -= 1
print(len(fishes))