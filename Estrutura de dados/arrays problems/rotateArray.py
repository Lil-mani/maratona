def jump(nums:list[int])->bool:
    i = 0
    querry = [0]
    while querry: 
        v = nums[querry.pop()]
        while v > 0:
            aux = len(nums)-1-nums[v]
            if aux == 0:
                return True 
            querry.append(v+i)
            v-=1



dici = {'fruit':['apple','banana']}
print(dici)


test1 = [2,3,1,1,4]
test2 = [3,2,1,0,4]
test3 = [1,2]

#print(jump(test2))