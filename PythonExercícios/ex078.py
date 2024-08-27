lista = []
for i in range(0,5):
    num = int(input("Digite um número: "))
    lista.append(num)

lista.sort()
maior = lista[4]
menor = lista[0]

print(f"O maior número digitado foi: {maior}.")
print(f"O menor número digitado foi: {menor}.")