# Coleta o preço
inicial = float(input("Qual o valor do produto?"))
# Calcula a procentagem
final =  float(inicial-(inicial*(5/100)))
print(f"O preço final do produto com o desconto é de R${final:.2f}")

