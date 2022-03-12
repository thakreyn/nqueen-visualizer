from drawtree import draw_bst
from main import render, screen, N
import time

def print_board(board):
    for row in board:
        print(*row)

def solve(board, col, left_row,lower_diagonal, upper_diagonal,N):
    if col == N:
        # print_board(board)
        # print('-'*15)
        render(screen,board,True)
        # time.sleep(0.5)
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

        # print_board(board)
        render(screen, board , False)

nums = [int(x) for x in range(20)]
draw_bst(nums)

# N = 4

board = [['.' for x in range(N)] for y in range(N)]
print_board(board)

left_row = [0 for x in range(N)]
upper_diagonal = [0 for x in range(2*N - 1)]
lower_diagonal = [0 for x in range(2*N - 1)]

solve(board, 0,left_row, lower_diagonal, upper_diagonal, N)


