# Cadastro de pessoas
homem = 0
mulher = 0
maior = 0

while True:
    print("-"*30)
    print("     CADASTRE UMA PESSOA     ")
    print("-"*30)

    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().lower()[0]

    if sexo == "m":
        homem += 1
    if sexo == "f" and idade < 20:
        mulher += 1
    if idade > 18:
        maior += 1

    print("-" * 30)
    resp = input("Deseja continuar? [S/N]").strip().lower()[0]
    if resp == "n":
        break

print(f"Total de pessoas com mais de 18 anos: {maior}.")
print(f"Ao todo temos {homem} homens cadastrados.")
print(f"E temos {mulher} mulheres com menos de 20 anos")
