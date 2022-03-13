import pygame
clock = pygame.time.Clock()
import test as t
import time

pygame.init()

# number of queens
N=8

# DIMENSIONS OF THE CHESS BOARD
GridSize = 75
screen_width = N * GridSize
screen_height = N * GridSize + 50

# setting caption and font 
pygame.display.set_caption('N-queen Visualizer')
font = pygame.font.SysFont("serif", 32*N//8)

def fillSquare(screen):
    '''make chess board'''
    
    for i in range(0,screen_width,GridSize):
        for j in range(0,screen_width,GridSize):
            if (i+j)%2==0:
                color=(240,240,240)
            else:
                color=(0,128,0)
                
            pygame.draw.rect(screen,color,pygame.Rect(i,j,GridSize,GridSize))


def placeQueens(screen,visited, solution):
    '''place queens accordng to the visited matrix we get from the solver'''

    if solution:
        img = pygame.image.load('images/queen2.png')
    else:
        img = pygame.image.load('images/queen.png')
    img = pygame.transform.scale(img, (GridSize, GridSize))
    
    for i in range(0,screen_width,GridSize):
        for j in range(0,screen_width,GridSize):
            if visited[i//GridSize][j//GridSize]=='Q':
                screen.blit(img, (i, j))


def scoreBar(no_of_iterations,found_solutions):
    '''Maintaing score bar'''

    sols = font.render('Solutions Found :' + str(found_solutions),21,(48,213,200))
    screen.blit(sols, ((N-N//2)*GridSize-13,screen_width+3))
    iter = font.render('Iterations :'+ str(no_of_iterations),21,(48,213,200))
    screen.blit(iter, (10,screen_width+3))
    pygame.display.flip()


def render(screen,visited=[], solution = False, no_of_iterations = 0, found_solutions = 0):
    '''Render the screen.
       Calls all the functions and update the screen.
    '''

    # to avoid overwriting or over-rendering
    screen.fill((0,0,0))

    fillSquare(screen)

    placeQueens(screen,visited, solution)

    scoreBar(no_of_iterations,found_solutions)
    pygame.display.flip()

screen = pygame.display.set_mode((screen_width, screen_height)) 
# Set up the drawing window


if __name__ == '__main__':
    
    # Run until the user asks to quit

    clock.tick(60)
    ev = pygame.event.poll()

    t.solve(t.board, 0,t.left_row,t.lower_diagonal,t.upper_diagonal, N)
    # Done! Time to quit.
    pygame.quit()

