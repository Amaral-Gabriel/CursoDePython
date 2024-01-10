# Antes de assistir a explicação, usando if
print("="*30)
print("         BANCO GAT      ")
print("="*30)

valor = int(input("Que valor você quer sacar? R$"))
cinquenta = valor // 50
resto50 = valor % 50
vinte = resto50 // 20
resto20 = resto50 % 20
dez = resto20 // 10
resto10 = resto20 % 10
um = resto10 // 1

if cinquenta > 0:
    print(f"Total de {cinquenta} cédulas de R$50.")
if vinte > 0:
    print(f"Total de {vinte} cédulas de R$20.")
if dez > 0:
    print(f"Total de {dez} cédulas de R$10.")
if um > 0:
    print(f"Total de {um} cédulas de R$1.")

print("Volte sempre ao BANCO GAT!")


# Depois da explicação usando while e if
print("="*30)
print("         BANCO GAT      ")
print("="*30)

valor = int(input("Que valor você quer sacar? R$"))
total = valor
ced = 50
totalced = 0

while True:

    if total >= ced:
        totalced += 1
        total -= ced
    else:
        if totalced > 0:
            print(f"Total de {totalced} cédulas de R${ced}.")
        if total < ced:
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            if total == 0:
                break
            totalced = 0
print("Volte sempre ao BANCO GAT!")
