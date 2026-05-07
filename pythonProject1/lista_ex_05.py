"""

"""
def contar_ficheiro(nome_ficheiro):
    linhas = 0
    palavras = 0
    vogais = 0
    consoantes = 0

    with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
        for linha in ficheiro:
            linhas += 1
            palavras += len(linha.split())

            for char in linha.lower():
                if char.isalpha():  # Verifica se é letra
                    if char in 'aeiouáàãâéêíóôõúç':
                        vogais += 1
                    else:
                        consoantes += 1

    return linhas, palavras, vogais, consoantes


# Nome do ficheiro
nome = "pensamento.txt"

l, p, v, c = contar_ficheiro(nome)

print("Número de linhas:", l)
print("Número de palavras:", p)
print("Número de vogais:", v)
print("Número de consoantes:", c)
