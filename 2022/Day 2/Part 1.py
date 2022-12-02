with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
winningMoves = {"A": "Y", "B": "Z", "C": "X"}
conversion = {"X": "A", "Y": "B", "Z": "C"}
points = {"X": 1, "Y": 2, "Z": 3}
score = 0
for line in lines:
    theirs, mine = line.split(" ")
    score += points[mine]
    if theirs == conversion[mine]: # Draw
        score += 3
    if winningMoves[theirs] == mine: # Win
        score += 6
print(score)