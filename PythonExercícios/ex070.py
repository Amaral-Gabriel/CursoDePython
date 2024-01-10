print("-"*30)
print("      Loja Super Baratão     ")
print("-"*30)


preco = 0
barato = " "
precoBarato = 0
soma = 0
caro = 0
cont = 0

while True:
    nome = input("Nome do produto: ").capitalize().strip()
    preco = float(input("Preço: R$"))
    soma += preco
    cont += 1
    if preco > 1000:
        caro += 1
    if cont == 1:
        barato = nome
        precoBarato = preco
    elif cont > 1:
        if precoBarato > preco:
            precoBarato = preco
            barato = nome
    resp = input("Deseja continuar? [S/N]: ").strip().lower()[0]
    if resp == "n":
        break
print(f"O total da compra foi: R${soma:.2f}.")
print(f"Temos {caro} produtos custando mais de R$1.000,00")
print(f"O produto mais barato foi {barato} que custou R${precoBarato:.2f}")





