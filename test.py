from typing import Iterator
from main import render, screen, N
import pygame

# Score Bar variables
no_of_iterations = 0
found_solutions = 0

# for debuggig purpose
def print_board(board):
    for row in board:
        print(*row)

# DFS logic 
def solve(board, col, left_row,lower_diagonal, upper_diagonal,N):
    
    global no_of_iterations, found_solutions

    # print(no_of_iterations, found_solutions)
    if col == N:
        found_solutions += 1

        # Calling render fucntion from main.py file 
        render(screen,board,True,no_of_iterations,found_solutions)
        
        # waiting for 2 sec when solution found. 
        pygame.time.wait(2000)
        return

    for row in range(N):
        no_of_iterations += 1
        if left_row[row] == 0 and lower_diagonal[row + col] == 0 and upper_diagonal[N-1 + col - row] == 0:
            
            board[row][col] = 'Q'
            left_row[row] = 1
            lower_diagonal[row + col] = 1
            upper_diagonal[N-1+col-row] = 1
            # recursive call
            solve(board, col+1, left_row, lower_diagonal, upper_diagonal, N)
            board[row][col] = '.'
            left_row[row] = 0
            lower_diagonal[row + col] = 0
            upper_diagonal[N-1+col-row] = 0
                
        # Calling render fucntion from main.py file 
        render(screen, board , False, no_of_iterations, found_solutions)

# declaring a N*N board 
board = [['.' for x in range(N)] for y in range(N)]

# lists for checking if the queen is safe or not 
left_row = [0 for x in range(N)]
upper_diagonal = [0 for x in range(2*N - 1)]
lower_diagonal = [0 for x in range(2*N - 1)]

solve(board, 0,left_row, lower_diagonal, upper_diagonal, N)


