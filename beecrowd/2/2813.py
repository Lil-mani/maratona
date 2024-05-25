n = int(input())
tempo = []
for i in range(n):
    tempo.append(input().split())

counterw = 0 
counterh = 0
umbrella = 0 
for i in range(n):
    umbrella-= 1
    if tempo[i][0] == "sol" and tempo[i][1] == "chuva":
        if umbrella < 0:
            counterw+=1 
            umbrella+=1
    elif tempo[i][0] == "chuva" and tempo[i][1] == "sol":
        umbrella+=1
        if umbrella < 0:
            counterh+=1
            

print(counterh,counterw)