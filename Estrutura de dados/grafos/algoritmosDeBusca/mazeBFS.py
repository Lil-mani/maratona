from queue import SimpleQueue

n = 0
m = 0


def is_cell_valid(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if board[x][y] == 1:
        return False
    if visited[x][y]:
        return False

    return True


def bfs(x, y):
    q = SimpleQueue()

    visited[x][y] = True
    q.put((x, y))

    while not q.empty():
        currentX, currentY = q.get()

        if is_cell_valid(currentX + 1, currentY):  # Check if we can go to the south
            visited[currentX + 1][currentY] = True
            q.put((currentX + 1, currentY))

        if is_cell_valid(currentX, currentY + 1):  # Check if we can go to the east
            visited[currentX][currentY + 1] = True
            q.put((currentX, currentY + 1))

        if is_cell_valid(currentX - 1, currentY):  # Check if we can go to the north
            visited[currentX - 1][currentY] = True
            q.put((currentX - 1, currentY))

        if is_cell_valid(currentX, currentY - 1):  # Check if we can go to the west
            visited[currentX][currentY - 1] = True
            q.put((currentX, currentY - 1))


n, m = map(int, input().split())

board = []  # board[i][j] = 1, if and only the cell (i,j) is broken
visited = [] 


for i in range(n):
    board.append(list(map(int, input().split())))

    # Initialize visited
    for _ in range(n):
        visited.append([0 for _ in range(m)])

qtd_components = 0

for x in range(n):
    for y in range(m):
        if (
            visited[x][y] or board[x][y] == 1
        ):  # Check if we have already visited self cell or if it is broken
            continue

        # We find a component

        bfs(x, y)  # Mark all cells in the component of the cell (x,y)
        qtd_components += 1  # Increase our answer by 1

print(f"Number of components: {qtd_components}")
