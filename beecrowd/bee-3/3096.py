from math import floor, log10,e,pi

n = int(input())

num_digitos = floor((n * log10(n / e)) + (log10(2 * pi * n) / 2.0)) + 1
print('{}'.format(num_digitos))