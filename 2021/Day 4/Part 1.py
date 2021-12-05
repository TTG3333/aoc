with open("Input.txt", "tr") as F:
    bingo = F.read().splitlines()

class Board:
    def __init__(self, rows):
        self.board = []
        for x in rows:
            self.board.append([[int(y), False] for y in x.split(" ") if y != ""])
    
    def checkRow(self, num):
        for x in self.board[num]:
            if x[1] == False:
                return False
        return True
    
    def checkCol(self, num):
        for x in self.board:
            if x[num][1] == False:
                return False
        return True
    
    def add(self, val):
        for row, x in enumerate(self.board):
            for col, y in enumerate(x):
                if y[0] == val:
                    self.board[row][col][1] = True
    
    def returnSumUnmarked(self):
        unmarked = 0
        for x in self.board:
            for y in x:
                if y[1] == False:
                    unmarked += y[0]
        return unmarked
    
    def __str__(self):
        return str(self.board)

nums = [int(x) for x in bingo[0].split(",")]
boards = []
for x in range((len(bingo[2:])+1)//6):
    boards.append(Board([bingo[2+6*x+y] for y in range(5)]))
for x in nums:
    for y, board in enumerate(boards):
        board.add(x)
        boards[y] = board
        for z in range(5):
            if board.checkCol(z) == True or board.checkRow(z) == True:
                print(board.returnSumUnmarked()*x)
                exit()