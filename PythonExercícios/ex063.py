print("=-=" * 15)
print("Sequência de Fibonacci")
print("=-=" * 15)
# Coleta a quantidades de números
n = int(input("Quantos números você quer ver?"))

f1 = 0
f2 = 1
cont = 3

print(f"{f1} --> {f2}",end=" --> ")

while cont <= n:
    f3 = f1 + f2
    print(f"{f3}",end=" --> ")
    f1 = f2
    f2 = f3
    cont += 1

print("Fim")
