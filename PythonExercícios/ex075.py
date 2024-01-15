# Coleta os valores
num = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o último número: ")),)
par = ()
# Mostra os valores digitados
print(f"Você digitou os valores:", end=' ')
for i in num:
    print(i, end=' ')
    if i % 2 == 0:
        par += num
# Mostra quantas ocorrências do 9
print(f"\nO número 9 apareceu {num.count(9)} vezes.")
# Mostra onde está o número 3
if 3 in num:
    print(f"O número 3 apareceu na {num.index(3) + 1}ª posição.")
else:
    print("O número 3 não foi digitado.")
# Mostra os valores pares
print("Os valores pares digitados foram: ", end=' ')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')





