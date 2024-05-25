'''
-- quando que achamos o minimo: quando tanto o elemento na direita quanto a esquerda dele forem maiores que ele
    -- se não forem, seguir a direção do menor elemento 
'''

def minimum(a):
    i = len(a)//2
    while a[i-1] < a[i] or a[i+1] < a[i]:
        if a[i-1] < a[i]:
            i = i-1
        elif a[i+1] < a[i]:
            i = i+1
    return a[i]



a = [4,5,6,7,0,1,2]
print(minimum(a))