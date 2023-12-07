# Coleta dados
sal = float(input("Qual o seu salário?: R$"))
imovel = float(input("Qual o valor do imóvel? R$"))
mes = int(input("Em quantos anos de financiamento?")) * 12
prest = imovel / mes
mini = sal * (30/100)
if mini < prest:
    print("Empréstimo \33[31mNEGADO!")
else:
    print("Empréstimo \33[32mCONCEDIDO!")

