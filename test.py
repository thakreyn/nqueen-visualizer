from main import render, screen, N
import time

def print_board(board):
    for row in board:
        print(*row)

def solve(board, col, left_row,lower_diagonal, upper_diagonal,N):
    if col == N:
        render(screen,board,True)
        return

    for row in range(N):
        if left_row[row] == 0 and lower_diagonal[row + col] == 0 and upper_diagonal[N-1 + col - row] == 0:
            board[row][col] = 'Q'
            left_row[row] = 1
            lower_diagonal[row + col] = 1
            upper_diagonal[N-1+col-row] = 1
            solve(board, col+1, left_row, lower_diagonal, upper_diagonal, N)
            board[row][col] = '.'
            left_row[row] = 0
            lower_diagonal[row + col] = 0
            upper_diagonal[N-1+col-row] = 0

        render(screen, board , False)

board = [['.' for x in range(N)] for y in range(N)]
print_board(board)

left_row = [0 for x in range(N)]
upper_diagonal = [0 for x in range(2*N - 1)]
lower_diagonal = [0 for x in range(2*N - 1)]

solve(board, 0,left_row, lower_diagonal, upper_diagonal, N)


