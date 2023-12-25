# Cria as variáveis
soma = 0
media = 0
mv = 0
nomeMV = ""
cont = 0
# Coleta os dados
for i in range(1, 5):
    print(f"----- {i}ª PESSOA -----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper().strip()
    # Soma a idade para conseguir a média depois
    soma += idade
    # Verifica se é homem para determinar o homem mais velho
    if sexo == "M":
        # Verifica se o homem é o mais velho
        if idade > mv:
            # Caso seja o mais velho define ele com a variável "nomeMV"
            mv = idade
            nomeMV = nome
    # Verifica se é mulher menor de idade de adiciona 1 ao contador
    if sexo == "F" and idade < 20:
        cont += 1

media = float(soma / 4)

print(f"A média de idade do grupo é de {media:.1f} anos!")
print(f"O homem mais velho tem {mv} anos e se chama {nomeMV}.")
print(f"Ao todo são {cont} mulheres com menos de 20 anos.")
