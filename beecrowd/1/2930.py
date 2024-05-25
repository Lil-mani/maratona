e,d = map(int,input().split())

if d-e >= 3:
    print('Muito bem! Apresenta antes do Natal!')
elif d-e <0:
    print("Eu odeio a professora!")

elif d-e <3:
        print('Parece o trabalho do meu filho!')
        d+=2
        if d>24:
            print("Fail! Entao eh nataaaaal!")
        else:
            print("TCC Apresentado!")
