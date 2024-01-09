print("=-="*15)
print("Os 10 primeiros termos de uma P.A.")
print("=-="*15)
# Coleta os dados
num = int(input("Digite o primeiro valor: "))
razao = int(input("Digite a razão da sua P.A.: "))
cont = 0
final = 0
# Utiliza o while para criar a P.A.
while cont != 10:
    # Estrutura para saber se é o último elemento
    if cont == 9:
        print(f"{num} --> PAUSA")
        cont += 1
        final = num
    else:
        print(f"{num}",end=" --> ")
        num += razao
        cont += 1

contNovo = 10
novaRazao = int(input("Quantos termos você quer a mais?"))
cont = 0

while novaRazao != 0:
    cont = 0
    contNovo += novaRazao
    while cont != novaRazao:
        # Estrutura para saber se é o último elemento
        if cont == novaRazao - 1:
            print(f"{num + razao} --> PAUSA")
            num += razao
            cont += 1
        else:
            print(f"{num + razao}", end=" --> ")
            num += razao
            cont += 1
    novaRazao = int(input("Quantos termos você quer a mais?"))
print(f"Progressão finalizada com {contNovo} itens visualizados!")
