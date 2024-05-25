a1,b1,a2,b2,a,b = input().split()
a1 = int(a1)
a2 = int(a2)
b1 = int(b1)
b2 = int(b2)
a = int(a)
b = int(b)

possivel = 'N'

# caso 1

aa1 = a1 + a2
bb1 = min(b1,b2)

if aa1 >= a:
    if bb1 >= b:
        possivel = 'S'
if bb1 >= a:
    if aa1 >= b:
        possivel = 'S'

# caso 2

ba2 = b1 + a2
ab2 = min(b2,a1)

if ba2 >= a:
    if ab2 >= b:
        possivel = 'S'
if ab2 >= a:
    if ba2 >= b:
        possivel = 'S'

# caso 3

bb3 = b1 + b2
aa3 = min(a1,a2)

if bb3 >= a:
    if aa3 >= b:
        possivel = 'S'
if aa3 >= a:
    if bb3 >= b:
        possivel = 'S'

# checa se o retangulo 1 é grande o suficiente para fazer o lençol

if a1 >= a:
    if b1 >= b:
        possivel = 'S'

if b1 >= a:
    if a1 >= b:
        possivel = 'S'

# checa se o retangulo 2 é grande o suficiente para fazer o lençol

if a2 >= a:
    if b2 >= b:
        possivel = 'S'

if b2 >= a:
    if a2 >= b:
        possivel = 'S'

print(possivel)