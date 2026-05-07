"""
. Considere o seguinte ficheiro de texto: (ou em formato csv separados por ; )

3 de 3

a. Quantas pessoas se encontram registadas?
b. Qual a quantidade de pessoas distribuídas pelas zonas do país (Norte,
Centro, Sul)?
c. Dada a zona do país, determine a média de idades.
d. Dado o nome de uma pessoa, mostrar onde ela vive (nome da cidade).
Deve mostrar todas as ocorrências do nome dado.


e. Dada uma cidade, calcular quantas pessoas lá vivem.
f. Qual a cidade com mais habitantes registados no ficheiro?
g. Determinar a quantidade de pessoas em todas as cidades e qual a
percentagem correspondente.
h. Dado o nome de uma cidade, perguntar se para a respetiva pessoa,
pretende mudar de cidade. Se sim, então deve substituir o nome da cidade
registado pelo nome da nova cidade.
i. Crie um novo ficheiro com a informação que está em memória, respeitando
o formato do csv.
"""
def ler_ficheiro(nome_ficheiro):
    pessoas = []
    with open(nome_ficheiro, 'r', encoding='utf-8') as f:
        for linha in f:
            nome, cidade, idade, zona = linha.strip().split(';')
            pessoas.append({
                "nome": nome,
                "cidade": cidade,
                "idade": int(idade),
                "zona": zona
            })
    return pessoas


# a) Quantas pessoas estão registadas?
def total_pessoas(pessoas):
    return len(pessoas)


# b) Quantidade de pessoas por zona
def pessoas_por_zona(pessoas):
    zonas = {"Norte": 0, "Centro": 0, "Sul": 0}
    for p in pessoas:
        zonas[p["zona"]] += 1
    return zonas


# c) Média de idades por zona
def media_idades_zona(pessoas, zona):
    idades = [p["idade"] for p in pessoas if p["zona"] == zona]
    if len(idades) == 0:
        return 0
    return sum(idades) / len(idades)


# d) Mostrar onde vive uma pessoa (todas as ocorrências)
def onde_vive(pessoas, nome):
    cidades = [p["cidade"] for p in pessoas if p["nome"] == nome]
    return cidades


# e) Quantas pessoas vivem numa cidade
def pessoas_na_cidade(pessoas, cidade):
    return sum(1 for p in pessoas if p["cidade"] == cidade)


# f) Cidade com mais habitantes
def cidade_mais_habitantes(pessoas):
    contagem = {}
    for p in pessoas:
        contagem[p["cidade"]] = contagem.get(p["cidade"], 0) + 1
    return max(contagem, key=contagem.get)


# g) Quantidade de pessoas por cidade + percentagem
def estatisticas_cidades(pessoas):
    total = len(pessoas)
    contagem = {}
    for p in pessoas:
        contagem[p["cidade"]] = contagem.get(p["cidade"], 0) + 1

    percentagens = {}
    for cidade, qtd in contagem.items():
        percentagens[cidade] = (qtd / total) * 100

    return contagem, percentagens


# h) Alterar cidade de uma pessoa
def mudar_cidade(pessoas, nome, nova_cidade):
    for p in pessoas:
        if p["nome"] == nome:
            p["cidade"] = nova_cidade


# i) Criar novo ficheiro com dados atualizados
def guardar_ficheiro(nome_ficheiro, pessoas):
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        for p in pessoas:
            linha = f"{p['nome']};{p['cidade']};{p['idade']};{p['zona']}\n"
            f.write(linha)


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

pessoas = ler_ficheiro("pessoas.csv")

print("a) Total de pessoas:", total_pessoas(pessoas))

print("b) Pessoas por zona:", pessoas_por_zona(pessoas))

print("c) Média de idades no Norte:", media_idades_zona(pessoas, "Norte"))

print("d) Onde vive José:", onde_vive(pessoas, "José"))

print("e) Pessoas em Bragança:", pessoas_na_cidade(pessoas, "Bragança"))

print("f) Cidade com mais habitantes:", cidade_mais_habitantes(pessoas))

contagem, percentagens = estatisticas_cidades(pessoas)
print("g) Pessoas por cidade:", contagem)
print("Percentagens:", percentagens)

# Exemplo de alteração
mudar = input("Quer mudar a cidade de alguém? (s/n) ")
if mudar.lower() == 's':
    nome = input("Nome da pessoa: ")
    nova = input("Nova cidade: ")
    mudar_cidade(pessoas, nome, nova)

guardar_ficheiro("novo_pessoas.csv", pessoas)
