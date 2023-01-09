
def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end =" ")
        print()
def isSafe (board, row, col, N):
    i=row 
    j = col
    while (i > -1 and j > -1):
        if (board[i][j] == 'Q'):
            return False
        i=i-1
        j=j-1
    i=row 
    j = col
    while (i > -1 and j < N):
        if (board[i][j] == 'Q'):
            return False
        i=i-1
        j =j+1
    i=row 
    j = col
    while (i > -1):
        if (board[i][j] == 'Q'):
            return False
        i=i-1
    return True
def solutionExists(board, N, row):
    if (row >= N):
        return True
    for col in range(N):
        if (isSafe(board, row, col, N)):
            board[row][col] = 'Q'
            if (solutionExists(board, N, row + 1)):
                return True
            board[row][col] = '.'
    return False
def solveNQueenProblem(N):
    board = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append('.')
        board.append(temp)
    if (solutionExists(board, N, 0) == False):
        print("No solution exists for N =", N)
    else:
        print("One of the possible solution for N =", N, "is -")
        printSolution(board, N)
N = int(input("Enter The Size of The Board : \n>>"))
solveNQueenProblem(N)
