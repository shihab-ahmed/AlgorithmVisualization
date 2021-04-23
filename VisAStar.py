import pygame
import sys

#https://github.com/nas-programmer/path-finding/blob/master/bfs.py

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
        self.parentNode = None
        self.rect = pygame.Rect(CELL_WIDTH * self.x, CELL_HEIGHT * self.y, CELL_WIDTH - 1, CELL_HEIGHT - 1)
        self.visited = False
        self.dist = 0
        self.block = False

    def add_neighbors(self, grid):
        if self.x > 0:
            self.neighbour.append(grid[self.x-1][self.y])
            # print(i - 1, j)
        if self.x < TOTAL_COL - 1:
            self.neighbour.append(grid[self.x+1][self.y])
            # print(i + 1, j)
        if self.y > 0:
            self.neighbour.append(grid[self.x][self.y-1])
            # print(i, j-1)
        if self.y < TOTAL_ROW - 1:
            self.neighbour.append(grid[self.x][self.y+1])

    def DrawNode(self):
        pygame.draw.rect(WINDOW, WHITE, self.rect)

    def DrawSelected(self):
        #print(self.rect)
        pygame.draw.rect(WINDOW, GREEN, self.rect)

    def DrawBlock(self):
        # print(self.rect)
        pygame.draw.rect(WINDOW, BLACK, self.rect)

    def DrawNeighbour(self):
        #print(self.rect)
        pygame.draw.rect(WINDOW, RED, self.rect)

    def DrawParent(self):
        #print(self.rect)
        pygame.draw.rect(WINDOW, YELLOW, self.rect)


def create_grid():
    for i in range(TOTAL_ROW):
        arr = []
        for j in range(TOTAL_COL):
            node = Node(i, j)
            node.DrawNode()
            arr.append(node)
        Grid.append(arr)


def add_neighbor():
    for i in range(TOTAL_ROW):
        for j in range(TOTAL_COL):
            Grid[i][j].add_neighbors(Grid)


def mousePos(pos):
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
        if Grid[p.x][p.y] == dest:
            return p.dist
        for i in range(len(Grid[p.x][p.y].neighbour)):
            if Grid[p.x][p.y].neighbour[i].visited == False:
                Grid[p.x][p.y].neighbour[i].visited = True
                Grid[p.x][p.y].neighbour[i].dist = p.dist + 1
                Grid[p.x][p.y].neighbour[i].parentNode=p
                print(Grid[p.x][p.y].neighbour[i].parentNode)
                queue.append(Grid[p.x][p.y].neighbour[i])
    return - 1

def ShowPath():
    for i in range(50):
        for j in range(50):
            print(Grid[i][j].block)


def main():
    WINDOW.fill((0, 20, 20))
    create_grid()
    add_neighbor()
    isDrawingWall = True
    source = Grid[0][0]
    dest = Grid[48][48]
    isPathFound = False
    source.DrawSelected()
    dest.DrawSelected()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if isDrawingWall:
                    col = event.pos[0] // CELL_WIDTH
                    row = event.pos[1] // CELL_HEIGHT
                    Grid[col][row].block = True
                    Grid[col][row].DrawBlock()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    isDrawingWall = False
                    queue.append(source)
                    source.visited = True
                    while len(queue) > 0 and not isPathFound:
                        p = queue.pop(0)
                        p.DrawNeighbour()
                        if Grid[p.x][p.y] == dest:
                            isPathFound=True
                        for i in range(len(Grid[p.x][p.y].neighbour)):
                            if Grid[p.x][p.y].neighbour[i].visited == False and not Grid[p.x][p.y].neighbour[i].block:
                                Grid[p.x][p.y].neighbour[i].visited = True
                                Grid[p.x][p.y].neighbour[i].dist = p.dist + 1
                                Grid[p.x][p.y].neighbour[i].parentNode = p
                                queue.append(Grid[p.x][p.y].neighbour[i])
                    if isPathFound:
                        current_node=dest
                        while current_node!=source:
                            current_node.DrawParent()
                            current_node=current_node.parentNode



        pygame.display.update()


if __name__ == "__main__":
    main()
