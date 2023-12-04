from random import sample
# Coleta o nome dos alunos
a1 = input("Qual o nome do primeiro aluno?")
a2 = input("Qual o nome de segundo aluno?")
a3 = input("Qual o nome do terceiro aluno?")
a4 = input("Qual o nome do quarto aluno?")
# Cria uma lista com os alunos
alunos = [a1, a2, a3, a4]

print(f"{sample(alunos, 4)}")
