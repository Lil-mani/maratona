entregadores2 = [10,10,10,10] # pizzas = 5 res = 20
pizzas2 = 5
# entregadores2 = [4,6,1] # pizzas = 7 res = 6 
entregadoresaux = entregadores2.copy()
# pizzas2 = 7

custo = float("inf")
for i in range(pizzas2):
    maisRapido = min(entregadoresaux)
    for j in range(len(entregadores2)):
        if entregadoresaux[j] <= maisRapido:
            maisRapido = entregadoresaux[j]
            entregadoresaux[j]+=entregadores2[j]
            break
    custo = maisRapido


print(custo)
