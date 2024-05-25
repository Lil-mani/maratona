t = int(input())
array = []
for _ in range(t):
    s = input()
    s = ''.join([char for char in s if not char.isupper()])
    s = s[::-1]
    print(s)
