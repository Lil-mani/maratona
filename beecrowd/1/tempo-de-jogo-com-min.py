n = int(input())
arr = list(map(int,input().split()))
cont1 = 0
cont0 = 0 
for i in arr:
    if i == 1: cont1+=1
    else: cont0+=1

if cont1 >= cont0: print("N")
else: print("S")