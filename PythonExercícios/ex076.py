lista = ("Lápis", 1.50,
         "Caneta", 2,
         "Caderno", 15.90,
         "Apontador", 3,
         "Estojo", 25,
         "Compasso", 9.90,
         "Livro", 34.90,
         "Mochila", 149.90)

print("=" * 40)
print(f"{'TABELA DE PREÇOS':^40}")
print("=" * 40)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end=' ')
    else:
        print(f"R${lista[i]:>7.2f}")
print("=" * 40)


