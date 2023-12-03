# Coleta dados
n = float(input("Quanto dinheiro voce tem?"))
# Calcula o valor em dolar (US$1,00 = R$3,27)
dolar = float(3.27)
conv = (n*dolar)
print(f"Com {int(n)} reais você pode comprar {conv:.2f} dolares!")

