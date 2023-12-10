from random import randint
from time import sleep
# Coleta a jogada
print("""Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
usu = int(input("Qual a sua jogada? "))
comp = randint(1,3)

print("JO")
sleep(1)
print("KEM")
sleep(1)
print("PO")
sleep(1)

if usu == 1:
    if comp == 1:
        print("Você jogou PEDRA e o computador também, então deu \33[33mEMPATE!")
    elif comp == 2:
        print("Você jogou PEDRA e o computador jogou PAPEL, então você \33[31mPERDEU!")
    elif comp == 3:
        print("Você jogou PEDRA e o computador jogou TESOURA, então você \33[32mGANHOU!")
elif usu == 2:
    if comp == 2:
        print("Você jogou PAPEL e o computador também, então deu \33[33mEMPATE!")
    elif comp == 3:
        print("Você jogou PAPEL e o computador jogou TESOURA, então você \33[31mPERDEU!")
    elif comp == 1:
        print("Você jogou PAPEL e o computador jogou PEDRA, então você \33[32mGANHOU!")
elif usu == 3:
    if comp == 3:
        print("Você jogou TESOURA e o computador também, então deu \33[33mEMPATE!")
    elif comp == 1:
        print("Você jogou TESOURA e o computador jogou PEDRA, então você \33[31mPERDEU!")
    elif comp == 2:
        print("Você jogou TESOURA e o computador jogou PAPEL, então você \33[32mGANHOU!")
