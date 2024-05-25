s = int(input())
score1 = 0
score2 = 0
for _ in range(s):
       sco = input().split()
       # reconhecer o 1 e 2
       if sco[1] == '1':
              score1+= int(sco[2])
              print(score1)
       else:
              score2+= int(sco[2])

print(score1," x ",score2)