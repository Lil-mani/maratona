res = []
maior_res = []

while True:
    try:
        test_cases = int(input())
        if test_cases == 0:
            break
        maior = 0
        for _ in range(test_cases):
            s = input().split()
            s = " ".join(s)
            res.append(s)
            maior = max(maior,len(s))

        maior_res.append(maior)

    except EOFError:
        break


for i in range(len(res)):
    n = maior - maior_res[i]
    tab = " " * n
    print(tab+res[i])

"""
https://judge.beecrowd.com/en/problems/view/1278
https://judge.beecrowd.com/en/problems/view/1273
"""