from datetime import date
# Coleta dados
ano = int(input("Qual o ano do seu nascimento? "))
atual = date.today().year
idade = atual - ano
if idade < 18:
    print(f"Você so tem {idade} anos. Você só precisará se alistar em \33[32m{18 - idade} anos\33[m em {ano + 18}.")
elif idade > 18:
    print(f"Você já tem {idade} anos. Você deveria ter se alistado a \33[31m{idade - 18} anos\33[m em {ano + 18}.")
elif idade == 18:
    print("Você tem que se alistar \33[33mIMEDIATAMENTE!")
