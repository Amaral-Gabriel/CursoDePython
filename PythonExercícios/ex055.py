maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f"O menor peso registrado foi {menor}Kg.")
print(f"O maior peso registrado foi {maior}Kg.")

