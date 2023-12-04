from math import hypot
# Coleta dados
c1 = float(input("Cateto oposto:"))
c2 = float(input("Cateto adjacente:"))
# Calcula a hipotenusa
hipo = hypot(c1,c2)
print(f"A hipotenusa vai medir {hipo:.2f}.")

