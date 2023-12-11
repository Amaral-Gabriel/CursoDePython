# Coleta os dados
print("=-=-=-=10 PRIMEIROS TERMOS DE UMA P.A.=-=-=-=")
num = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))

for c in range(num, (num + 9 * raz) + raz, raz):
    print(f"{c} --> ", end="")
print("Acabou!")

