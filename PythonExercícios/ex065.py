# Define a resposta do usuário com "s" por padrão
resp = "s"
cont = 0
soma = 0
maior = menor = 0

while resp != "n":
    # Solicita o número
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    # Verifica se é o primeiro número e define ele como maior e menor ao mesmo tempo
    if cont == 1:
        maior = num
        menor = num
    # Caso não seja o primeiro, entra nas condicionais que comparam e definem o maior e o menor
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input("Deseja continuar? (S/N)").lower().strip()

media = soma / cont

print(f"Você digitou {cont} números e a média foi {media:.1f}!")
print(f"O menor valor foi {menor} e o maior foi {maior}.")
