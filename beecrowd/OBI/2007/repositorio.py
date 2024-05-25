c,n = map(int,input().split())

arquivosAtuais = {}
arquivosAtualizados = {}

for i in range(c):
    arquivo,versao = map(int,input().split())
    arquivosAtuais[arquivo] = versao

for i in range(n):
    arquivo,versao = map(int,input().split())

    if arquivo not in arquivosAtuais:
        arquivosAtuais[arquivo] = versao
        arquivosAtualizados[arquivo] = versao
    
    elif int(versao) > arquivosAtuais[arquivo]:
        arquivosAtuais[arquivo] = versao
        arquivosAtualizados[arquivo] = versao


for arquivo in sorted(arquivosAtualizados):
    print(arquivo,arquivosAtualizados[arquivo])

