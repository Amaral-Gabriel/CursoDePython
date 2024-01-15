palavras = ("aprender", "python", "curso", "video",
            "programar", "trabalhar", "estudar", "gratis",
            "praticar", "linguagem", "futuro", "mercado",)
for i in palavras:
    print(f"\nNa palavra {i.upper()} temos", end=" ")
    for vogal in i:
        if vogal.lower() in "aeiou":
            print(f"{vogal}", end=" ")

