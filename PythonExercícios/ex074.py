from random import randint
tupla = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20),)
print(f"Os números sorteados foram: ",end="")
for i in tupla:
    print(f"{i}",end=" ")

print(f"\nO maior valor foi {max(tupla)}.")
print(f"O menor valor foi {min(tupla)}.")



