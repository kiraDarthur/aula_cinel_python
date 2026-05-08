lista = []
with open("alunos.txt", "r") as fp:
    for linha in fp:
        dados = linha.strip().split(";")
        nome = dados[0]
        numero = int(dados[1])
        if numero >= 10:
            print(f"Os alunos aprovados foram: {nome}")






