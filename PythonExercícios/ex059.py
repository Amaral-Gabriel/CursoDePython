# Coleta os números
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa""")
op = int(input("Selecione uma opção: "))
print("=-="*15)

while op != 5:
    if op == 1:
        print(f"A soma entre {n1} e {n2} é igual a {n1 + n2}.")
    elif op == 2:
        print(f"A multiplicação entre {n1} e {n2} é igual a {n1 * n2}.")
    elif op == 3:
        if n1 > n2:
            print(f"O maior número é {n1}.")
        if n1 < n2:
            print(f"O maior número é {n2}.")
        if n1 == n2:
            print("Os dois números são iguais.")
    elif op == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    else:
        print("Opção inválida! Tente novamente.")
    print("=-="*15)
    print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa""")
    op = int(input("Selecione uma opção: "))
    print("=-="*15)
print("Programa encerrado com sucesso!")
