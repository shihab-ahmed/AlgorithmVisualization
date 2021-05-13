import random

import pygame
import sys

pygame.init()

# Screen Properties
WIDTH = 800
HEIGHT = 800
SCREEN_SIZE = (WIDTH, HEIGHT)
WINDOW = pygame.display.set_mode(SCREEN_SIZE)
FPS = 60
Clock = pygame.time.Clock()
TOTAL_COL = 40
TOTAL_ROW = 40
CELL_WIDTH = WIDTH // TOTAL_COL
CELL_HEIGHT = HEIGHT // TOTAL_ROW
pygame.display.set_caption("Algorithm Vis")

BLACK = (0, 0, 0)
DARK_BLUE = (4, 24, 34)
GREEN = (0, 255, 25)
LIME = (0, 220, 95)
RED = (255, 0, 0)
PINK = (255, 0, 205)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)

Grid = []
path = []
queue = []
visited = []
cost = {}


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
        self.weight = random.randint(1, 5)

    def add_neighbors(self, grid):
        if self.x > 0:
            self.neighbour.append(grid[self.x - 1][self.y])
        if self.x < TOTAL_COL - 1:
            self.neighbour.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbour.append(grid[self.x][self.y - 1])
        if self.y < TOTAL_ROW - 1:
            self.neighbour.append(grid[self.x][self.y + 1])

    def DrawNode(self):
        DARK_BLUE = (56, 84 + self.weight * 5, 112)
        pygame.draw.rect(WINDOW, DARK_BLUE, self.rect)

    def DrawVisited(self):
        pygame.draw.rect(WINDOW, GREEN, self.rect)

    def DrawBlock(self):
        pygame.draw.rect(WINDOW, BLACK, self.rect)

    def DrawQueue(self):
        pygame.draw.rect(WINDOW, LIME, self.rect)

    def DrawPath(self):
        pygame.draw.rect(WINDOW, CYAN, self.rect)

    def DrawSourceAndDestination(self):
        pygame.draw.rect(WINDOW, PINK, self.rect)


def create_grid():
    for i in range(TOTAL_ROW):
        arr = []
        for j in range(TOTAL_COL):
            node = Node(i, j)
            cost[node] = 10000
            arr.append(node)
        Grid.append(arr)


def add_neighbor():
    for i in range(TOTAL_ROW):
        for j in range(TOTAL_COL):
            Grid[i][j].add_neighbors(Grid)


def close():
    print("Closing")
    pygame.quit()
    sys.exit()


def get_min_cost():
    min_node = next(iter(cost))
    for x in cost:
        if cost[min_node] > cost[x] and not x.visited:
            min_node = x
    return min_node


def show_update(source, destination):
    count=0
    WINDOW.fill(BLACK)
    for i in range(TOTAL_ROW):
        for j in range(TOTAL_COL):
            node = Grid[i][j]
            node.DrawNode()
            if node in path:
                node.DrawPath()
            elif node.visited:
                node.DrawVisited()
                count+=1
            elif node in queue:
                node.DrawQueue()
            elif node.block:
                node.DrawBlock()
            elif node == source:
                node.DrawSourceAndDestination()
            elif node == destination:
                node.DrawSourceAndDestination()
            pass
    print(count)
    pygame.display.flip()


def main():
    WINDOW.fill((0, 20, 20))
    create_grid()
    add_neighbor()
    isDrawingWall = True
    source = Grid[30][30]
    destination = Grid[30][39]
    isPathFound = False
    show_update(source, destination)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3):
                    if isDrawingWall:
                        col = event.pos[0] // CELL_WIDTH
                        row = event.pos[1] // CELL_HEIGHT
                        if Grid[col][row] != source and Grid[col][row] != destination:
                            Grid[col][row].block = True
                            show_update(source, destination)
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    if isDrawingWall:
                        col = event.pos[0] // CELL_WIDTH
                        row = event.pos[1] // CELL_HEIGHT
                        if Grid[col][row] != source and Grid[col][row] != destination:
                            Grid[col][row].block = True
                            show_update(source, destination)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    isDrawingWall = False
                    current_node = source
                    cost[current_node] = 0
                    while current_node != destination:
                        for node in current_node.neighbour:
                            if node.weight + cost[current_node] < cost[node] and not node.block:
                                cost[node] = node.weight + cost[current_node]
                                node.parentNode = current_node
                        if not current_node.visited:
                            current_node.visited = True
                            current_node = get_min_cost()
                        if current_node == destination:
                            isPathFound = True
                            break
                        show_update(source, destination)
                    if isPathFound:
                        current_node = destination
                        while current_node != source:
                            path.append(current_node)
                            current_node = current_node.parentNode
                            show_update(source, destination)


if __name__ == "__main__":
    main()
