from datetime import date
# Coleta o ano de nascimeto
nasc = int(input("Qual o ano do seu nascimento? "))
# Calcula a idade
atual = date.today().year
idade = atual - nasc
clas = str()

if idade <= 9:
    clas = "MIRIM"
elif idade > 9 and idade <= 14:
    clas = 'INFANTIL'
elif idade > 14 and idade <= 19:
    clas = 'JÚNIOR'
elif idade > 19 and idade <= 25:
    clas = 'SÊNIOR'
else:
    clas = "MASTER"

print(f"O atleta tem {idade} anos.")
print(f"Classificação: {clas}")


