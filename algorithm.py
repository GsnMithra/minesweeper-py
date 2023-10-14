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

def mineSweepUtil (board, i, j, count, clone, hit):
    if count <= 0 and hit:
        return
    if min (i, j) < 0 or i >= len (board) or j >= len (board[0]) or board[i][j] != 'E':
        return
    
    currMines = mineCount (board, i, j)
    if currMines != 0:
        board [i][j] = clone[i][j]
    else:
        hit = True
        board [i][j] = 'B'
    
        dx = [0, 0, 1, -1, -1, 1, -1, 1]
        dy = [1, -1, 0, 0, -1, 1, 1, -1]

        for s in range (8):
            newX = i + dx [s]
            newY = j + dy [s]

            mineSweepUtil (board, newX, newY, count - 1, clone, hit)

def updateBoard (board, click, clone):
    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
        return board

    mineSweepUtil (board, click[0], click[1], random.randint (1, 15), clone, False)
    if board[click[0]][click[1]] != 'M' or board[click[0]][click[1]] != 'E':
        setMineCounts (board, click[0], click[1])
    return board

def setMineCounts (board, X, Y):
    visited = set ()
    queue = list ()
    queue.append ((X, Y))

    while queue:
        curr = queue.pop (0)

        dx = [0, 0, 1, -1, -1, 1, -1, 1]
        dy = [1, -1, 0, 0, -1, 1, 1, -1]

        for i in range (7):
            currX, currY = dx[i], dy[i]
            if (currX, currY) not in visited:
                if board[currX][currY] == 'B':
                    currMines = mineCount (board, currX, currY)
                    if currMines == 0:
                        board[currX][currY] = 'B'
                    else:
                        board[currX][currY] = str (currMines)
                    visited.add ((currX, currY))
                    queue.append ((currX, currY))

def clonedGridValues (grid):
    for i in range (len (grid)):
        for j in range (len (grid)):
            if grid[i][j] == 'E':
                minesCount = mineCount (grid, i, j)
                grid[i][j] = 'B' if minesCount == 0 else str (minesCount)
    return grid