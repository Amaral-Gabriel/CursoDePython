print("=-="*15)
print("Os 10 primeiros termos de uma P.A.")
print("=-="*15)
# Coleta os dados
num = int(input("Digite o primeiro valor: "))
razao = int(input("Digite a razão da sua P.A.: "))
cont = 0
# Utiliza o while para criar a P.A.
while cont != 10:
    # Estrutura para saber se é o último elemento
    if cont == 9:
        print(f"{num} --> FIM")
        cont += 1
    else:
        print(f"{num}",end=" --> ")
        num += razao
        cont += 1




