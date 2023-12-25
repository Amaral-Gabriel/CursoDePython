# Coleta a entrada
sexo = input("Digite seu sexo [M/F]: ").upper()
while sexo != "M" and sexo != "F":
    sexo = input("Dados inválidos! Tente novamente. Digite seu sexo [M/F]: ").upper()
print(f"Sexo {sexo} registrado com sucesso!")
