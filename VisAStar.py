import pygame
import sys
#https://github.com/nas-programmer/path-finding/blob/master/astar.py

pygame.init()

#Screen Properties
WIDTH=800
HEIGHT=600
SCREEN_SIZE=(WIDTH,HEIGHT)
WINDOW=pygame.display.set_mode(SCREEN_SIZE)
FPS=60
Clock = pygame.time.Clock()
COL=50
ROW=50
CELL_WIDTH=WIDTH//COL
CELL_HEIGHT=WIDTH//ROW
pygame.display.set_caption("Algorithm Vis")

Grid=[]
Path=[]

class Node:
    def __init__(self,row,col):
        pass


def DrawGrid(GRID):
    pass

def __main__():
    for i in range(50):
        for j in range(50):
            pygame.Rect(1)
            #pygame.draw.rect(WINDOW, col, (self.x * w, self.y * h, w - 1, h - 1))
    pass

def close():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    __main__()