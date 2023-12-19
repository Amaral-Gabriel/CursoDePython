# Coleta frase
frase = input("Digite uma palavra ou frase e veja se é um palíndromo ou não: ").upper().strip()
# Separa a frase em uma lista
sep = frase.split()
# Junta todas as palavras
junto = "".join(sep)[::-1]
print(f"{frase} de trás pra frente é {junto}")
if junto[::-1] == junto:
    print("Isso é um palíndromo!")
else:
    print("Isso não é um palíndromo!")




