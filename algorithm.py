import random

def mineCount (board, i, j):
    i -= 1
    j -= 1
    mines = 0
    
    for c in range (i, i + 3):
        for r in range (j, j + 3):
            if 0 <= c < len (board) and 0 <= r < len (board[0]) and board[c][r] == 'M':
                mines += 1
    return mines

def mineSweepUtil (board, i, j, count):
    if count == 0:
        return
    if min (i, j) < 0 or i >= len (board) or j >= len (board[0]) or board[i][j] != 'E':
        return
    
    currMines = mineCount (board, i, j)
    if currMines != 0:
        board [i][j] = str (currMines)
    else:
        board [i][j] = 'B'
    
        dx = [0, 0, 1, -1, -1, 1, -1, 1]
        dy = [1, -1, 0, 0, -1, 1, 1, -1]

        for s in range (8):
            newX = i + dx [s]
            newY = j + dy [s]

            mineSweepUtil (board, newX, newY, count - 1)

def updateBoard (board, click):
    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
        return board

    mineSweepUtil (board, click[0], click[1], random.randint (1, 10))
    return board