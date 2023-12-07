# Coleta os dados
seg1 = float(input("Segmento 1: "))
seg2 = float(input("Segmento 2: "))
seg3 = float(input("Segmento 3: "))
# Organiza em uma lista crescente
lista = [seg1, seg2, seg3]
lista.sort()
soma = lista[0] + lista[1]

if soma > lista[2]:
    print("Essas retas formam um triângulo!")
else:
    print("Essas retas não formam um triângulo!")
