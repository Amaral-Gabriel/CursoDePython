# Tabuada dentro do while, acaba com números negativos
while True:
    print("-"*40)
    num = int(input("Quer ver a tabuada de qual valor?"))
    print("-" * 40)
    if num < 0:
        break
    for c in range(0, 11):
        print(f"{num} X {c:2} = {num * c:2}")
print("Programa da tabuada encerrado.")
