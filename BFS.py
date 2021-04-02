from random import randrange

MapSizeX = 20
MapSizeY = 20

grid = [['*', '0', '*', '*', '*', '0', '*', '0', '0', '*', '*', '0', '*', '*', '*', '0', '*', '0', '0', '*'],
        ['*', '*', '*', '0', '*', '*', '0', '0', '0', '0', '*', '*', '0', '*', '*', '0', '*', '0', '0', '0'],
        ['*', '0', '*', '0', '0', '0', '0', '*', '*', '*', '0', '*', '0', '*', '0', '*', '*', '0', '0', '0'],
        ['0', '0', '0', '0', '*', '0', '*', '0', '0', '*', '*', '*', '0', '*', '*', '0', '0', '*', '*', '0'],
        ['0', '*', '*', '*', '*', '*', '0', '*', '0', '*', '0', '0', '0', '0', '0', '*', '0', '*', '*', '0'],
        ['*', '0', '*', '0', '*', '0', '0', '*', '*', '0', '*', '0', '*', '*', '*', '*', '0', '0', '*', '0'],
        ['*', '*', '*', '0', '*', '0', '*', '*', '0', '0', '0', '*', '0', '*', '*', '0', '0', '*', '*', '0'],
        ['*', '*', '0', '*', '*', '0', '*', '0', '0', '*', '0', '0', '*', '0', '*', '*', '*', '*', '0', '*'],
        ['0', '*', '0', '*', '0', '0', '0', '*', '*', '*', '0', '0', '0', '*', '0', '*', '0', '*', '*', '*'],
        ['*', '*', '*', '0', '*', '0', '*', '0', '*', '*', '0', '0', '0', '0', '*', '*', '0', '0', '0', '*'],
        ['0', '*', '*', '0', '0', '0', '0', '0', '0', '*', '0', '0', '0', '*', '*', '*', '*', '*', '0', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '0', '0', '0', '0', '*', '0', '0', '*', '*', '*', '*', '0'],
        ['0', '0', '0', '*', '*', '*', '0', '0', '*', '0', '0', '0', '0', '*', '0', '*', '0', '*', '*', '0'],
        ['*', '0', '0', '0', '0', '*', '*', '*', '*', '0', '*', '*', '*', '*', '0', '*', '0', '*', '*', '*'],
        ['*', '*', '0', '0', '0', '0', '*', '*', '*', '0', '*', '0', '*', '*', '*', '0', '0', '*', '*', '0'],
        ['0', '0', '0', '*', '*', '0', '0', '0', '*', '0', '*', '0', '*', '*', '*', '*', '*', '0', '*', '0'],
        ['*', '0', '0', '*', '*', '0', '0', '0', '0', '0', '0', '0', '0', '0', '*', '0', '0', '*', '0', '0'],
        ['*', '*', '*', '0', '0', '*', '*', '*', '*', '0', '0', '0', '0', '*', '0', '0', '0', '*', '0', '*'],
        ['0', '0', '*', '*', '*', '*', '0', '*', '0', '*', '0', '*', '*', '*', '0', '0', '0', '0', '*', '*'],
        ['s', '*', '*', '*', '*', 'd', '0', '0', '0', '0', '0', '0', '*', '*', '0', '0', '*', '0', '0', '*']]


# Class for node
class QItem:
    def __init__(self, row, col, dist, ):
        self.row = row
        self.col = col
        self.dist = dist


visited = [[False for x in range(MapSizeX)] for y in range(MapSizeY)]
queueList = []
source = QItem(0, 0, 0)
destination = QItem(0, 0, 0)

for x in range(MapSizeX):
    for y in range(MapSizeY):
        if grid[x][y] == "s":
            source.row = x
            source.col = y
        elif grid[x][y] == "d":
            destination.row = x
            destination.col = y


def bfs():
    queueList.append(source)
    visited[source.row][source.col] = True
    while len(queueList) > 0:
        p = queueList.pop(0)
        if grid[p.row][p.col] == "d":
            return p.dist
        # Move up
        if (p.row - 1) >= 0 and visited[(p.row - 1)][p.col] == False and grid[p.row - 1][p.col] != "0":
            queueList.append(QItem(p.row - 1, p.col, p.dist + 1))
            visited[(p.row - 1)][p.col] = True
            # print([p.row - 1, p.col])
        # Move down
        if (p.row + 1) < MapSizeX and visited[(p.row + 1)][p.col] == False and grid[p.row + 1][p.col] != "0":
            queueList.append(QItem(p.row + 1, p.col, p.dist + 1))
            visited[(p.row + 1)][p.col] = True
            # print([p.row + 1, p.col])
        # Move left
        if (p.col - 1) >= 0 and visited[p.row][p.col - 1] == False and grid[p.row][p.col - 1] != "0":
            queueList.append(QItem(p.row, p.col - 1, p.dist + 1))
            visited[p.row][p.col - 1] = True
            # print([p.row, p.col-1])
        # Move right
        if (p.col + 1) < MapSizeY and visited[p.row][p.col + 1] == False and grid[p.row][p.col + 1] != "0":
            queueList.append(QItem(p.row, p.col + 1, p.dist + 1))
            visited[p.row][p.col + 1] = True
            # print([p.row, p.col+1])
        # print("......................................")
    return - 1


print(bfs())
