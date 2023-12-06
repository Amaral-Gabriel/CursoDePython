# Coleta a velocidade
vel = float(input("Qual a velocidade atual do carro? "))
multa = (vel - 80) * 7
if vel > 80:
    print(f"Cuidado. Você está acima da velocidade permitida e vai pagar uma multa de R${multa:.2f}!")
else:
    print("Faça uma boa viagem!")
