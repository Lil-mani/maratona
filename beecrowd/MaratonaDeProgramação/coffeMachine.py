p = int(input())
s = int(input())
t = int(input())

op1 = s*2 + t*4
op2 = p*2 + t*2
op3 = p*4 + s*2

resultado = min(op1,op2)
resultado = min(resultado,op3)
print(resultado)

