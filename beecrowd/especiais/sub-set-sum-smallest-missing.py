"""
artigo de estudo: https://medium.com/dexters-lab/eli5-find-the-smallest-positive-integer-value-that-cannot-be-represented-as-sum-of-any-subset-of-f8ea2488184b

"""

t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()

    maxPossible = 0

    if len(array) == 0 or array[0] !=1:
        print(maxPossible+1)
    else:
    
        maxPossible = 1

        for i in range(1,n):
            if array[i] <= maxPossible+1:
                maxPossible+=array[i]
        
        print(maxPossible+1)