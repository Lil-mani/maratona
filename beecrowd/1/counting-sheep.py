t = int(input())
res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    setezinho = set(arr)
    print(len(setezinho))