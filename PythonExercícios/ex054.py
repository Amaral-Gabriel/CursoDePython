from datetime import date
# Cria as variáveis
menor = 0
maior = 0
cont = 1
idade = date.today().year - 18
# Coleta as idades
for i in range(0, 7):
    ano = int(input(f"Digite o ano de nascimento da {cont}º pessoa: "))
    cont += 1
    if ano <= idade:
        print("Essa pessoa é maior de idade.")
        maior += 1
    else:
        menor += 1
        print("Essa pessoa é menor de idade.")
if maior == 0:
    print("Todos ainda são de menores de idade.")
elif menor == 0:
    print("Todos já são de maiores de idade.")
else:
    print(f"Ao todo tivemos {maior} pessoa/as maiores de idade.")
    print(f"E também tivemos {menor} pessoa/as menores de idade.")


