try:
    with open("facts.txt", "r", encoding="utf-8") as file:
        facts = [line.rstrip() for line in file]
except FileNotFoundError:
    print(
        "Файл facts.txt не найден. Добавьте файл с фактами, чтобы боту было, о чём рассказывать"
    )
