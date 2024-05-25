import sys
sys.setrecursionlimit(10**9)
n,m,x,y,k = map(int,input().split())
mat = [[0 for x in range(m+1)] for y in range(n+1)] 
res = 0 

for _ in range(k):
    a,b = map(int,input().split())
    mat[a][b] = 1

def dfs(v,t):
    global res 

    if v>n or t >m or t<1 or v<1 or mat[v][t] == 1: return

    mat[v][t] = 1
    res+=1

    for i in range(v-1,v+2):
        for j in range(t-1,t+2):
            dfs(i,j)

dfs(x,y)
print(res)


