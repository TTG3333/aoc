with open("Input.txt", "tr") as F:
    actions = F.read().splitlines()
accumulator = 0
current_action = 0
completed_actions = []
while True:
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
print(accumulator)