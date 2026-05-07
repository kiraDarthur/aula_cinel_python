print("A")
#ler o ficheiro
with open("dados", "r") as ficheiro:
    conteudo = ficheiro.read()
    print(conteudo)


#escrever o ficheiro e apagar
with open ("dados", "w") as ficheiro:
    ficheiro.write("ola mundo\n")
    ficheiro.write("nova linha ")


#somente escrever
with open("dados", "a") as ficheiro:
    ficheiro.write("\ntexto adiciona\n ")
print("\nB")

#ler linha por linha
with open("dados", "r") as ficheiro:
    for linha in ficheiro:
        print(linha.strip())
print("\n\nC")
#mais exercicios
#escrever no arquivo
with open("nome", "w") as f:
    f.write("ana\n")
    f.write("arthur\n")
    f.write("eliane\n")
#ler
with open("nome","r") as f:
    for nome in f:
        print("nome:",nome.strip())