with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
winningMoves = {"A": "B", "B": "C", "C": "A"}
losingMoves = {"A": "C", "B": "A", "C": "B"}
points = {"A": 1, "B": 2, "C": 3}
score = 0
for line in lines:
    theirs, outcome = line.split(" ")
    if outcome == "X": # Lose
        score += points[losingMoves[theirs]]
    if outcome == "Y": # Draw
        score += 3 + points[theirs]
    if outcome == "Z": # Win
        score += 6 + points[winningMoves[theirs]]
print(score)