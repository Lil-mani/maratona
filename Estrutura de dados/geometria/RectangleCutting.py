'''
7
1 1 --- NO
2 1 --- NO
2 6 --- YES
3 2 --- YES
2 2 --- YES
2 4 --- YES
4 2 --- YES
6 3 --- NO

'''

def Cutting(a,b):
    if a%2 == 0:
        if a/2 > b or a/2 < b:
            return "YES"
        elif b%2 == 0 and (b/2 > a or b/2 < a):
            return "YES"
        else:
            return "NO"
    elif b%2 == 0:
        if b/2 > a or b/2 < a:
            return "YES"
        else:
            return "NO"
    return "NO"

cases = int(input())
arr = []
for _ in range(cases):
    a,b = map(int,input().split())
    arr.append([a,b])

for _ in range(len(arr)):
    print(Cutting(arr[_][0],arr[_][1]))