def testActions(actions):
    accumulator = 0
    current_action = 0
    completed_actions = []
    while current_action < len(actions):
        for z in completed_actions:
            if current_action == z:
                break
        else:
            completed_actions.append(current_action)
            action = actions[current_action].split(" ")
            if action[0] == "acc":
                accumulator += int(action[1])
            elif action[0] == "jmp":
                current_action += int(action[1])
                continue
            current_action += 1
            continue
        break
    else:
        return accumulator
    return False

with open("Input.txt", "tr") as F:
    actions_raw = F.read()
actions = actions_raw.splitlines()
action_lists = []
jmp_indexes = []
nop_indexes = []
for y, x in enumerate(actions):
    action = x.split(" ")[0]
    if action == "jmp":
        jmp_indexes.append(y)
    elif action == "nop":
        nop_indexes.append(y)
for x in jmp_indexes:
    new_actions = actions_raw.splitlines()
    new_actions[x] = "nop " + new_actions[x].split(" ")[1]
    action_lists.append(new_actions)
for x in nop_indexes:
    new_actions = actions_raw.splitlines()
    new_actions[x] = "jmp " + new_actions[x].split(" ")[1]
    action_lists.append(new_actions)
for x in action_lists:
    result = testActions(x)
    if result == False:
        continue
    print(result)
    break