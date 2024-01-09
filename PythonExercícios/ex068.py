from random import randint

print("=-="*15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-="*15)

vitoria = 0
opcao = " "

while True:
    usu = int(input("Digite um valor: "))

    while opcao not in "PpIi":
        opcao = input("Par ou Ímpar? [P / I]").lower().strip()[0]

    comp = randint(0, 10)

    total = usu + comp

    if total % 2 == 0:
        resul = "p"  # par
        print(f"Você jogou {usu} e o computador jogou {comp}, o total de {total} PAR!")
        print("-" * 30)
    else:
        resul = "i"  # ímpar
        print(f"Você jogou {usu} e o computador jogou {comp}, o total de {total} ÍMPAR!")
        print("-" * 30)
    if resul == opcao:
        print(f"Você VENCEU!")
        print("-" * 30)
        vitoria += 1
    if resul != opcao:
        print(f"Você PERDEU!")
        print("-" * 30)
        break
    opcao = " "

print(f"GAME OVER. Você ganhou {vitoria} vezes!")
print("-" * 30)
