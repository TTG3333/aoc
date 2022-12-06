with open("Input.txt", "tr") as F:
    data = F.read()

for i in range(3, len(data)):
    if len(set([x for x in data[i-3:i+1]])) == 4:
        print(i+1)
        break
else:
    print(None)