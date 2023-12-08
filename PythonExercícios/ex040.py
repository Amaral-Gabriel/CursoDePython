# Coleta as notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota:"))
# Calcula a média
med = (n1 + n2) / 2
if med >= 7:
    print(f"A média do aluno é {med:.1f}.")
    print("O aluno está \33[32mAPROVADO\33[m!")
elif med < 7 and med >= 5:
    print(f"A média do aluno é {med:.1f}.")
    print("O aluno está em \33[33mRECUPERAÇÃO\33[m!")
elif med < 5:
    print(f"A média do aluno é {med:.1f}.")
    print("O aluno está \33[31mREPROVADO\33[m!")


