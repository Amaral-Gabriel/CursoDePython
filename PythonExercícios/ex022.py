# Coleta o nome
nome = input("Qual o seu nome? ")
print(f"Seu nome em maiusculo é {nome.upper()}.")
print(f"Seu nome em minusculo é {nome.lower()}.")
print(f"Seu nome tem {(len(nome))-nome.count(' ')} letras.")
print(f"O seu primeiro nome é {nome.split()[0]} que tem {len(nome.split()[0])} letras.")

