import pygame
import sys

# https://github.com/nas-programmer/path-finding/blob/master/astar.py

pygame.init()

# Screen Properties
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
WINDOW = pygame.display.set_mode(SCREEN_SIZE)
FPS = 60
Clock = pygame.time.Clock()
TOTAL_COL = 50
TOTAL_ROW = 50
CELL_WIDTH = WIDTH // TOTAL_COL
CELL_HEIGHT = HEIGHT // TOTAL_ROW
pygame.display.set_caption("Algorithm Vis")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 0, 205)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)

Grid = []
Path = []
queue = []


class Node:
    def __init__(self, row, col):
        self.x = row
        self.y = col
        self.neighbour = []
        self.parent = None
        self.rect = pygame.Rect(CELL_WIDTH * self.x, CELL_HEIGHT * self.y, CELL_WIDTH - 1, CELL_HEIGHT - 1)
        self.visited = False
        self.dist = 0

    def DrawNode(self):
        pygame.draw.rect(WINDOW, WHITE, self.rect)

    def DrawSelected(self):
        #print(self.rect)
        pygame.draw.rect(WINDOW, GREEN, self.rect)

    def DrawNeighbour(self):
        #print(self.rect)
        pygame.draw.rect(WINDOW, RED, self.rect)

    def DrawPath(self):
        #print(self.rect)
        pygame.draw.rect(WINDOW, YELLOW, self.rect)


def CreateGrid():
    for i in range(TOTAL_ROW):
        nodeArr = []
        for j in range(TOTAL_COL):
            node = Node(i, j)
            node.DrawNode()
            nodeArr.append(node)
            if i > 0:
                node.neighbour.append(Node(i - 1, j))
                #print(i - 1, j)
            if i < TOTAL_COL - 1:
                node.neighbour.append(Node(i + 1, j))
                #print(i + 1, j)
            if j > 0:
                node.neighbour.append(Node(i, j - 1))
                #print(i, j-1)
            if j < TOTAL_ROW-1:
                node.neighbour.append(Node(i, j + 1))
                #print(i, j+1)
        Grid.append(nodeArr)


def MousePos(pos):
    col = pos[0] // CELL_WIDTH
    row = pos[1] // CELL_HEIGHT

    Grid[col][row].DrawSelected()
    for i in range(len(Grid[col][row].neighbour)):
        Grid[col][row].neighbour[i].DrawNeighbour()


def close():
    print("Closing")
    pygame.quit()
    sys.exit()


def bfs(source, dest):
    queue.append(source)
    source.visited = True
    while len(queue) > 0:
        p = queue.pop(0)
        p.DrawNeighbour()
        #print(p.x,p.y)
        if Grid[p.x][p.y] == dest:
            return p.dist
        for i in range(len(Grid[p.x][p.y].neighbour)):
            if Grid[p.x][p.y].neighbour[i].visited == False:
                Grid[p.x][p.y].neighbour[i].visited = True
                Grid[p.x][p.y].neighbour[i].dist = p.dist + 1
                Grid[p.x][p.y].neighbour[i].parent=p
                queue.append(Grid[p.x][p.y].neighbour[i])
    return - 1

def ShowPath(source,dest,pos):
    col = pos[0] // CELL_WIDTH
    row = pos[1] // CELL_HEIGHT

    print(Grid[col][row].parent)


def main():
    WINDOW.fill((0, 20, 20))
    CreateGrid()
    check = False
    Source=None
    Dest=None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // CELL_WIDTH
                row = event.pos[1] // CELL_HEIGHT
                #MousePos(event.pos)
                if(Source==None):
                    Source=Grid[col][row]
                    print(Source)
                elif(Dest==None):
                    Dest = Grid[col][row]
                    print(Dest)
                if Source!=None and Dest!=None and not check:
                    if(bfs(Source,Dest)>0):
                        check =True
                elif check:
                    ShowPath(Source, Dest, event.pos)

        pygame.display.flip()


if __name__ == "__main__":
    main()
