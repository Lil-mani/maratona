n,k = map(int,input().split())

array = list(map(int,input().split()))
dic = {0:1}
prefix = 0
contador = 0
for i in range(n):
    prefix+=array[i]
    if prefix-k in dic:
        contador += dic[prefix-k]
    dic[prefix]= dic.get(prefix,0) + 1

print(contador)