# Coleta o valor
print(f"{"LOJAS GUANABARA":=^40}")
inicial = float(input("Preço das compras? R$"))
# Calcula os valores
pix = inicial - (inicial * (10/100))
c1x = inicial - (inicial * (5/100))
c2x = inicial
c3x = inicial + (inicial * (20/100))

print("""FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro ou pix
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opc = int(input("Digite a opção: "))

if opc == 1:
    print(f"Sua compra de R${inicial:.2f} vai custar R${pix:.2f} à vista no dinheiro ou pix.")
elif opc == 2:
    print(f"Sua compra de R${inicial:.2f} vai custar R${c1x:.2f} em 1x no cartão.")
elif opc == 3:
    print(f"Sua compra de R${inicial:.2f} vai custar R${c2x:.2f} e será dividida em 2 parcelas de {(c2x / 2):.2f}.")
elif opc == 4:
    parcela = int(input("Quantas parcelas?"))
    print(f"Sua compra de R${inicial:.2f} vai custar R${c3x:.2f} e será dividida em {parcela} de {(c3x / parcela):.2f}")
