contNum = 0
cont = 0

while True:
    num = int(input("Digite um número (999 para parar): "))
    if num == 999:
        break
    contNum += num
    cont += 1
print(f"A soma dos {cont} valores foi {contNum}!")
