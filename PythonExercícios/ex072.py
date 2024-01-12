# Coleta e valida o número
n = ("zero", "um", "dois", "três", "quatro", "cinco",
     "seis", "sete", "oito", "nove", "dez", "onze",
     "doze", "treze", "cartorze", "quinze", "dezesseis",
     "dezessete", "dezoito", "dezenove", "vinte")
num = int(input("Digite um número entre 0 e 20: "))
cont = "s"
while cont == "s":
    while True:
        if 20 >= num >= 0:
            print(f"Você digitou o número {n[num]}.")
            break
        else:
            num = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    # Verifica se o usuário deseja continuar
    cont = input("Deseja continuar? [S/N]").lower().strip()[0]
    if cont == "n":
        break
    else:
        # Solicita o novo numero para o while da linha 9
        num = int(input("Digite um número entre 0 e 20: "))
