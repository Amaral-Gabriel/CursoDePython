# Coleta os dados
seg1 = float(input("Segmento 1: "))
seg2 = float(input("Segmento 2: "))
seg3 = float(input("Segmento 3: "))
# Organiza em uma lista crescente
lista = [seg1, seg2, seg3]
lista.sort()
soma = lista[0] + lista[1]

if soma > lista[2]:
    if seg1 == seg2 == seg3:
        print("Essas retas formam um triângulo EQUILÁTERO!")
    elif seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
        print("Essas retas formam um triângulo ESCALENO!")
    else:
        print("Essas retas formam um triângulo ISÓCELES!")
else:
    print("Essas retas não formam um triângulo!")
