import random
print("Você consegue advinhar o número que eu pensei?")
# Coleta a resposta
usu = int(input("Escolha um úmero de 1 a 5: "))
# Escolhe um número aleatorio
num = random.randint(1, 5)
if usu <= 0 or usu >= 6:
    print("Escolha um número de 1 a 5. Tente novamente.")
else:
    if usu == num:
        print("Parabéns, você ganhou!")
        print(f"O número escolhido foi {num}.")
    else:
        print("Você perdeu!")
        print(f"O número escolhido foi {num}.")
