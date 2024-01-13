times = ("Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo",
         "Bragantino", "Fluminense", "Athletico-PR", "Internacional", "Fortaleza",
         "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", "Vasco",
         "Bahia", "Santos", "Goiás", "Coritiba", "América-MG",)



print("=-=" * 15)
print(f"Os times do Brasileirão 2023 foram: {times}")
print("=-=" * 15)
print(f"Os 5 primeiros colocados foram: {times[0:5]}")
print("=-=" * 15)
print(f"Os 4 últimos foram: {times[-4:]}")
print("=-=" * 15)
print(f"Times em ordem alfabética: {sorted(times)}")
print("=-=" * 15)
# Qual posição o São Paulo ficou?
print(f"O São Paulo ficou na {times.index("São Paulo")+1}ª posição.")
print("=-=" * 15)
