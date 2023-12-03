# Coleta os dados
larg = float(input("Qual a largura da sua parede?"))
altu = float(input("Qual a altura da sua parede?"))
# Calcula a area
area = (larg*altu)
tin = (area/2)
print(f"Para pintar {area:.2f} metros de parede, você precisará de {tin:.2f} litros de tinta.")
