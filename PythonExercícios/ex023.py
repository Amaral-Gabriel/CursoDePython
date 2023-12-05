# Coleta o número
num = int(input("Digite um número entre 0 e 9999: "))
# Calcula os valores
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print(f"Unidade: {uni}.")
print(f"Dezena: {dez}.")
print(f"Centena: {cen}.")
print(f"Milhar: {mil}.")
