class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(board, r):
            row = []
            for j in range(9):
                if board[r][j].isdigit():
                    row.append(board[r][j])
            return len(row) == len(set(row))

        def checkCol(board, c):
            col = []
            for i in range(9):
                if board[i][c].isdigit():
                    col.append(board[i][c])
            return len(col) == len(set(col))

        def checkSquare(board,r,c):
            square = []
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j].isdigit():
                        if board[i][j] in square:
                            return False
                        else:
                            square.append(board[i][j])
            return True

        row, col, square = True, True, True
        for r in range(9):
            row = row and checkRow(board,r)
            if not row:
                break
        for c in range(9):
            col = col and checkCol(board,c)
            if not col:
                break
        for i in range(0,7,3):
            for j in range(0,7,3):
                square = square and checkSquare(board,i,j)
                if not square:
                    break

        return row and col and square
        