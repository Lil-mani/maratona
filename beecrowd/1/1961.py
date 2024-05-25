p,n = map(int,input().split())
pipes = list(map(int,input().split()))

resposta = "YOU WIN"
for i in range(1,len(pipes)):
    if pipes[i] > pipes[i-1]:
        valorsubir = pipes[i-1] + p
        if valorsubir < pipes[i]:
            resposta = "GAME OVER"
            break
    elif pipes[i]<pipes[i-1]:
        valordescer = pipes[i-1] - pipes[i]
        if valordescer > p:
            resposta = "GAME OVER"
            break
    

print(resposta)
