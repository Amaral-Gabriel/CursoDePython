# Coleta o número
num = int(input("Digite um número de descubra o seu fatorial: "))
cont = num
i = num

print(f"Calculando o fatorial de {num}! = {num}",end="")
while i != 1:
    cont = cont * (i - 1)
    i -= 1
    print(f" X {i}",end="")
print(f" = {cont}",end="")


