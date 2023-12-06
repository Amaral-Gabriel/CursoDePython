# Coleta a distâcia
dis = int(input("Qual a distâcia da sua viagem? "))
curta = 0.50    # ate 200km
longa = 0.45
if dis <= 200:
    print(f"O valor da sua passagem é R${dis * curta:.2f}!")
else:
    print(f"O valor da sua passagem é R${dis * longa:.2f}!")


