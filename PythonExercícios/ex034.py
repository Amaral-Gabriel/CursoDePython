# Coleta o salário
sal = float(input("Digite seu salário: "))
# Calcula o salário
alto = sal * (10/100) + sal
baixo = sal * (15/100) + sal

print(f"Você passará a ganhar R${alto:.2f}!") if sal > 1250 else print(f"Você passará a ganhar R${baixo:.2f}!")



