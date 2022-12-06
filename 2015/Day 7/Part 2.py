from string import digits

with open("Input.txt", "tr") as F:
    links = F.read().splitlines()

wires = {}
for link in links:
    temp, dest = link.split(" -> ")
    temp = temp.split(" ")
    if len(temp) == 1:
        temp = temp[0]
        if temp[0] in digits:
            wires[dest] = {"value": int(temp)}
        else:
            wires[dest] = {"value": None, "expr": [temp], "expr_type": "EQ"}
    elif len(temp) == 2: # Can only be a NOT of another wire
        temp = temp[1]
        wires[dest] = {"value": None, "expr": [temp], "expr_type": "NOT"}
    else: # temp has 3 elements
        wires[dest] = {"value": None, "expr": [int(x) if x[0] in digits else x for x in temp[::2]], "expr_type": temp[1]}

def calcWire(obj, wires):
    if wires[obj]["value"] != None:
        return
    for x in wires[obj]["expr"]:
        if not isinstance(x, int):
            calcWire(x, wires)
    match wires[obj]["expr_type"]:
        case "EQ":
            wires[obj]["value"] = wires[wires[obj]["expr"][0]]["value"]
        case "NOT":
            wires[obj]["value"] = 2**16-1 - wires[wires[obj]["expr"][0]]["value"]
        case "AND":
            vals = [x if isinstance(x, int) else wires[x]["value"] for x in wires[obj]["expr"]]
            wires[obj]["value"] = vals[0] & vals[1]
        case "OR":
            vals = [x if isinstance(x, int) else wires[x]["value"] for x in wires[obj]["expr"]]
            wires[obj]["value"] = vals[0] | vals[1]
        case "LSHIFT":
            vals = [x if isinstance(x, int) else wires[x]["value"] for x in wires[obj]["expr"]]
            wires[obj]["value"] = vals[0] << vals[1]
        case "RSHIFT":
            vals = [x if isinstance(x, int) else wires[x]["value"] for x in wires[obj]["expr"]]
            wires[obj]["value"] = vals[0] >> vals[1]

calcWire("a", wires)
a_val = wires["a"]["value"]

wires = {}
for link in links:
    temp, dest = link.split(" -> ")
    temp = temp.split(" ")
    if len(temp) == 1:
        temp = temp[0]
        if temp[0] in digits:
            wires[dest] = {"value": int(temp)}
        else:
            wires[dest] = {"value": None, "expr": [temp], "expr_type": "EQ"}
    elif len(temp) == 2: # Can only be a NOT of another wire
        temp = temp[1]
        wires[dest] = {"value": None, "expr": [temp], "expr_type": "NOT"}
    else: # temp has 3 elements
        wires[dest] = {"value": None, "expr": [int(x) if x[0] in digits else x for x in temp[::2]], "expr_type": temp[1]}
wires["b"] = {"value": a_val}

calcWire("a", wires)
print(wires["a"]["value"])