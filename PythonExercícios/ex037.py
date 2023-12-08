num = int(input("Digite um número: "))
print("""Escolha uma opção:
[ 1 ] Converter para binário
[ 2 ] Converter para hexadecimal
[ 3 ] Converter para octal""")
opc = int(input("Sua opção: "))
if opc == 1:
    print(f"{num} convertido para BINÁRIO é {num:b}.")
elif opc == 2:
    print(f"{num} convertido para HEXADECIMAL é {num:x}.")
elif opc == 3:
    print(f"{num} convertido para OCTAL é {num:o}.")
else:
    print("Opção inválida! Tente novamente.")
