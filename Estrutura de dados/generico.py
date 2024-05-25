# n,m = map(int,input().split())

# casas = list(map(int,input().split()))
# entregas = set(x for x in input().split())



n = int(input())

aux = 10
while n > 9:
    print(n)
    n = int(n/10) *3 + n%10

print(n)




