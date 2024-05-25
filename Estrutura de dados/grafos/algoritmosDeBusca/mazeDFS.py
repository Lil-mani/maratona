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


def dfs(x, y):
    visited[x][y] = True

    if is_cell_valid(x + 1, y):  # Check if we can go to the south
        dfs(x + 1, y)

    if is_cell_valid(x, y + 1):  # Check if we can go to the east
        dfs(x, y + 1)

    if is_cell_valid(x - 1, y):  # Check if we can go to the north
        dfs(x - 1, y)

    if is_cell_valid(x, y - 1):  # Check if we can go to the west
        dfs(x, y - 1)


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

        dfs(x, y)  # Mark all cells in the component of the cell (x,y)
        qtd_components += 1  # Increase our answer by 1

print(f"Number of components: {qtd_components}")
