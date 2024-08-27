resp = True
lista = []

while resp:
    num = int(input("Digite um número: "))
    lista.append(num)
    entrada = input("Deseja continuar? (S/N) ")
    if entrada == "N":
        resp = False
    
lista.sort()
lista.reverse()

print(f"Você digitou {len(lista)} números")
print(f"Esse são os números em ordem descrecente: {lista}")

if 5 in lista:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")
