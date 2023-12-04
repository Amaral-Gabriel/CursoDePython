# Coleta dados
dias = int(input("Quanto dias alugados?"))
km = float(input("Quantos KM rodados?"))
# Calcula o valor
total = float((dias * 60) + (km * 0.15))

print(f"O valor do aluguel é de R${total:.2f}.")
