resp = True
lista = []

while resp:
    num = int(input("Digite um número: "))
    if not num in lista:
        lista.append(num)
    entrada = input("Deseja continuar? (S/N) ")
    if entrada == "N":
        resp = False
    
lista.sort()
print(f"Você digitou: {lista}")
