import time
class queen:
    def __init__(self, size):
        # board => dimensions size x size
        self.size = size 
        # columns[r] is a number c if a queen is placed at row r and column c.
        # columns[r] is out of range if no queen is place in row r.
        # Thus after all queens are placed, they will be at positions
        # (columns[0], 0), (columns[1], 1), ... (columns[size - 1], size - 1)
        self.columns = []
 
    def addInNextRow(self, column):
        self.columns.append(column)
 
    def currentRowRemove(self):
        return self.columns.pop()
 
    def checkPosition(self, column):
        # index of next row
        row = len(self.columns)
 
        # check column
        for queen_column in self.columns:
            if column == queen_column:
                return False
 
        # check diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False
 
        # check other diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row == (self.size - column) - row):
                return False
        return True
 
    def displayBoard(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('[👑]', end='')
                else:
                    print('[  ]', end='')
            print()
 
def solve_queen(size):
    chessBoard = queen(size)
    possibleSolutions = 0
 
    row = 0
    column = 0
    # iterating rows
    while 1>0:
        # place queen in next row
        while column < size:
            if chessBoard.checkPosition(column):
                chessBoard.addInNextRow(column)
                row += 1
                column = 0
                break
            else:
                column += 1
 
        # if column not found or board full
        if (column == size or row == size):
            # if board is full but we have a solution
            if row == size:
                chessBoard.displayBoard()
                print()
                possibleSolutions += 1
 
                chessBoard.currentRowRemove()
                row -= 1
            try:
                prev_column = chessBoard.currentRowRemove()
            except IndexError:
                # all queens removed => no more possible configurations
                break
            # trying previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column
 
    print('Number of Possible solutions: ', possibleSolutions)
n = int(input('Enter Size: '))
start = time.time()
solve_queen(n)
end = time.time()
print("Execution Time:", end-start,"s")