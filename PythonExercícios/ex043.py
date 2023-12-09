# Coleta dados
peso = float(input("Qual o seu peso? (kg)"))
altura = float(input("Qual a sua altura? (m)"))
# Calcula o IMC
imc = peso / (altura**2)
print(f"O IMC dessa pessoa é de {imc:.1f}.")
if imc < 18.5:
    print("Você está abaixo do peso normal!")
elif imc >= 18.5 and imc < 25:
    print("Parabéns! Seu peso é ideal.")
elif imc >= 25 and imc < 30:
    print("Cuidado, você está com sobre peso!")
elif imc >=30 and imc < 40:
    print("Cuidado você está com obesidade!")
else:
    print("Cuidado, Você está com obesidade mórbida!")

