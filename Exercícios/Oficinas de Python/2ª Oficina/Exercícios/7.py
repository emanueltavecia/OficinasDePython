# EXERCÍCIO 7:

# Crie um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
# Requisito: utilizar o comando for.

# Resolução:

s = 0
for c in range(6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos números pares é {s}')
