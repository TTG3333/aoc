with open("Input.txt", "tr") as F:
    data = F.read().splitlines()

time = int(data[0])
buses = []
for x in data[1].split(","):
    if x != "x":
        buses.append(int(x))

busWaitTime = []
for x in buses:
    bus = {"number": x}
    timeSinceBus = time%x
    if timeSinceBus == 0:
        bus["waitTime"] = 0
    else:
        bus["waitTime"] = x-timeSinceBus
    busWaitTime.append(bus)
busWaitTime.sort(key=lambda a: a["waitTime"])
print(busWaitTime[0]["number"]*busWaitTime[0]["waitTime"])