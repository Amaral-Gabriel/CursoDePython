# Coleta o nome
nome = input("Qual o seu nome completo? ").rstrip().lstrip()
dividido = nome.split()

print(f"Seu primeiro nome é {dividido[0]}.")
print(f"Seu último nome é {dividido[-1]}.")

