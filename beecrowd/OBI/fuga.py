n, m = map(int, input().split())
li, lf, ci, cf = 0, 0, 0, 0
lf, cf = map(int, input().split())
li, ci = map(int, input().split())

dl = [0, 0, -1, +1]
dc = [-1, +1, 0, 0]

custo = 0
resp = 0
grid = [[0] * m for _ in range(n)]

def dfs(l, c, custo):
    global resp
    grid[l][c] = 1
    custo += 1
    if l == lf and c == cf:
        resp = max(resp, custo)
    else:
        for i in range(4):
            nl, nc = l + dl[i], c + dc[i]
            if 0 <= nl < n and 0 <= nc < m and grid[nl][nc] == 0:
                dfs(nl, nc, custo)
    grid[l][c] = 0  # Desmarca o ponto após explorar todos os caminhos possíveis

dfs(li, ci, custo)
print(resp)
