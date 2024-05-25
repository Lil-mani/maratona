t = int(input())

for _ in range(t):
    r, s = input().split()

    if r == s:
        print('empate')
    elif (r == 'tesoura' and (s == 'papel' or s == 'lagarto')) or \
         (r == 'papel' and (s == 'pedra' or s == 'Spock')) or \
         (r == 'pedra' and (s == 'lagarto' or s == 'tesoura')) or \
         (r == 'lagarto' and (s == 'spock' or s == 'papel')) or \
         (r == 'spock' and (s == 'tesoura' or s == 'pedra')):
        print('rajesh')
    else:
        print('sheldon')
