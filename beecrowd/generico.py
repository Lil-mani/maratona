media = 0
p = 0
while True:
    try:
        s = input()
        media += int(input())
        p+=1
    except EOFError:
        break 

res = media/p
print(f"{res:.1f}")
