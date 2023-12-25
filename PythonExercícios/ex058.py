import random
print("Olá, sou seu computador.")
print("Eu acabei de pensar em um número entre 0 e 10.")
print("Você consegue advinhar o número que eu pensei?")
# Coleta a resposta
usu = int(input("Escolha um número de 0 a 10: "))
# Escolhe um número aleatorio
num = random.randint(1, 5)
cont = 1
while usu > 10 or usu < 0:
    usu = int(input("Lembre que é um número entre 0 e 10. Tente novamente: "))

while num != usu:

    if num > usu:
        usu = int(input("Mais... Tente novamente: "))
        while usu > 10 or usu < 0:
            usu = int(input("Lembre que é um número entre 0 e 10. Tente novamente: "))
    else:
        usu = int(input("Menos... Tente novamente: "))
        while usu > 10 or usu < 0:
            usu = int(input("Lembre que é um número entre 0 e 10. Tente novamente: "))
    cont += 1
print(f"Parabéns, você acertou em {cont} tentativas!")

