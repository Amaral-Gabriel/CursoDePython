lista = list()
for i in range(5):
    num = int(input("Digite o numero: "))
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        for pos, x in enumerate(lista):
            if num <= x:
                lista.insert(pos, num)
                break
print(lista)

