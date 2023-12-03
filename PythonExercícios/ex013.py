# Coleta o salario inicial
inicial = float(input("Digite o salário inicial:"))
# Calcula o aumento
final = float(inicial+(inicial*(15/100)))
print(f"Parabéns, você recebeu um aumento de 15%, a partir de agora você receberá R${final:.2f}!")
