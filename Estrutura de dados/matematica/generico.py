def Permutation(s):
    resultado = []
    visites = [False] * len(s)
    
    pass

test_cases = int(input())
res = []
for _ in range(test_cases):
    s = input()
    permutations = Permutation(s)
    for i in range(len(permutations)):
        res.appen("".join(permutations[i]))
