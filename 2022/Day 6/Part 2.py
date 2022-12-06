with open("Input.txt", "tr") as F:
    data = F.read()

for i in range(13, len(data)):
    if len(set([x for x in data[i-13:i+1]])) == 14:
        print(i+1)
        break
else:
    print(None)