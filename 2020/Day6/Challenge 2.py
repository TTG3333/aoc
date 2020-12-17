with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()
refined_answers = []
answer_text = ""
for y, x in enumerate(lines):
    if y == len(lines)-1:
        refined_answers.append(x)
    else:
        if x == "":
            refined_answers.append(answer_text[:-1])
            answer_text = ""
        else:
            answer_text += (x + "\n")
answer_count = 0
for x in refined_answers:
    questions = "abcdefghijklmnopqrstuvwxyz"
    for y in questions:
        if x.count(y) == len(x.splitlines()):
            answer_count += 1
print(answer_count)