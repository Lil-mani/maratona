# Questão facil 
n = int(input())
qualificados = int(input())
array = []
for _ in range(n):
    i = int(input())
    array.append(i)

array.sort(reverse=True)
totalFinalistas = qualificados
ultimoQualificado = array[qualificados-1]
i = qualificados
while i<len(array) and array[i] == ultimoQualificado:
    i+=1
    totalFinalistas+=1


print(totalFinalistas)

