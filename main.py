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
screen_height = N * GridSize


def fillSquare(screen):

    for i in range(0,screen_width,GridSize):
        for j in range(0,screen_height,GridSize):
            if (i+j)%2==0:
                color=(240,240,240)
            else:
                color=(0,128,0)
                # print(color)
            pygame.draw.rect(screen,color,pygame.Rect(i,j,GridSize,GridSize))
            
def placeQueens(screen,visited, solution):
    if solution:
        img = pygame.image.load('images/queen2.png')
    else:
        img = pygame.image.load('images/queen.png')
    img = pygame.transform.scale(img, (GridSize, GridSize))
    
    for i in range(0,screen_width,GridSize):
        for j in range(0,screen_height,GridSize):
            if visited[i//GridSize][j//GridSize]=='Q':
                screen.blit(img, (i, j))

    # if solution:
    #     pygame.time.wait(2000)

def render(screen,visited=[], solution = False):
    '''make chess board'''
    fillSquare(screen)

    '''place queens accordng to the visited matrix we get from the solver'''
    placeQueens(screen,visited, solution)


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

