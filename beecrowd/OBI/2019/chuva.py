n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)]

def is_valid(i, j):
    return 0 <= i < n and 0 <= j < m

for i in range(n):
    for j in range(m):
        if mat[i][j] == ".":
            if i > 0 and mat[i-1][j] == "o":
                mat[i][j] = "o"
            elif is_valid(i, j-1) and mat[i][j-1] == "o" and (is_valid(i+1, j-1) and mat[i+1][j-1] == "#"):
                mat[i][j] = "o"
            elif is_valid(i, j+1) and mat[i][j+1] == "o" and (is_valid(i+1, j+1) and mat[i+1][j+1] == "#"):
                mat[i][j] = "o"

for i in range(n):
    for j in range(m):
        if mat[i][j] == ".":
            if i > 0 and mat[i-1][j] == "o":
                mat[i][j] = "o"
            elif is_valid(i, j-1) and mat[i][j-1] == "o" and (is_valid(i+1, j-1) and mat[i+1][j-1] == "#"):
                mat[i][j] = "o"
            elif is_valid(i, j+1) and mat[i][j+1] == "o" and (is_valid(i+1, j+1) and mat[i+1][j+1] == "#"):
                mat[i][j] = "o"

for row in mat:
    print("".join(row))
