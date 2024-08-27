resp = True
lista = []
lista_par = []
lista_impar = []

while resp:
    num = int(input("Digite um número: "))
    lista.append(num)
    if num % 2 == 0 or num == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    entrada = input("Deseja continuar? (S/N) ")
    if entrada == "N":
        resp = False
    
print(f"Lista geral: {lista}")
print(f"Lista de pares: {lista_par}")
print(f"Lista de impares: {lista_impar}")