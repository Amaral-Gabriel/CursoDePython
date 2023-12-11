# Coleta o número
num = int(input("Digite um número: "))
cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(f"\33[32m{c}\33[m", end=" ")
        cont += 1
    else:
        print(f"\33[31m{c}\33[m", end=" ")

if cont == 2:
    print(f"\nO número {num} foi dividido {cont} vezes. Então ele é primo!")
else:
    print(f"\nO número {num} foi dividido {cont} vezes. Então ele NÃO é primo!")

