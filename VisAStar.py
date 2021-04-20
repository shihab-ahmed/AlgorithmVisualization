import pygame
import sys
#https://github.com/nas-programmer/path-finding/blob/master/astar.py

pygame.init()

#Screen Properties
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH,HEIGHT)
WINDOW = pygame.display.set_mode(SCREEN_SIZE)
FPS = 60
Clock = pygame.time.Clock()
TOTAL_COL=50
TOTAL_ROW=50
CELL_WIDTH=WIDTH//TOTAL_COL
CELL_HEIGHT=HEIGHT//TOTAL_ROW
pygame.display.set_caption("Algorithm Vis")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

Grid=[]
Path=[]

class Node:
    def __init__(self,row,col):
        self.x=row
        self.y=col
        self.neighbour=[]
        self.parent=None
    def DrawNode(self):
        rect = pygame.Rect(CELL_WIDTH * self.x, CELL_HEIGHT * self.y, CELL_WIDTH - 1, CELL_HEIGHT - 1)
        pygame.draw.rect(WINDOW, WHITE, rect)
        pass
    def add_neighbour(self):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])

def CreateGrid(GRID):
    for i in range(50):
        for j in range(50):
            node = Node(i,j)

def MousePos(pos):
    print(pos[0],pos[1])

def main():
    WINDOW.fill((0, 20, 20))
    DrawGrid(10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos[0])
                print(pygame.mouse.get_pressed(5))
                pass


        pygame.display.flip()

def close():
    print("Closing")
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()