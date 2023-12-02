n = input('Digite algo: ')
print(f'''
    O tipo primitivo desse valor é: {type(n)}
    Só tem espaços? {n.isspace()}
    É um número? {n.isnumeric()}
    É alfabético? {n.isalpha()}
    É alfanumérico? {n.isalnum()}
    Está em maiúsculas? {n.isupper()}
    Está em minúculas? {n.islower()}
    Está capitalizada? {n.istitle()}
       
''')