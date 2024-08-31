expre = str(input('Digite uma expressão: '))
cont = 0 

for i in expre:
    if i == '(':
        cont += 1
    elif i == ')':
        cont -= 1
        if cont < 0:
            print('Expressão inválida')
            exit(0)

if cont != 0: 
    print('Expressão inválida')
else:
    print('Expressão válida')