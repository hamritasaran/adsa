def solvequeens(N):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, N)):
            if board[i][j] == 'Q':
                return False
        return True

    def solve(row):
        if row == N:
            solutions.append(["".join(row) for row in board])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(row + 1)
                board[row][col] = '.'
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(0)
    
    return solutions
def print_solutions(solutions):
    for idx, solution in enumerate(solutions, start=1):
        print(f"Solution {idx}:")
        for row in solution:
            print(row)
N = 4
solutions = solvequeens(N)
print_solutions(solutions)
