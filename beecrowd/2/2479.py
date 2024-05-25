n = int(input())
count_good = 0
count_bad = 0
res = []
for _ in range(n):
    name = input().split()
    if name[0] == "+":
        count_good+=1
        res.append(name[1])
    else:
        count_bad+=1
        res.append(name[1])

res.sort()
for i in res:
    print(i)
print("Se comportaram: {} | Nao se comportaram: {}".format(count_good,count_bad))
