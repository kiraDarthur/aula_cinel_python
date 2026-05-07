
#Crie um programa que solicite ao utilizador o seu nome completo.
nome = input("Digite seu nome")
#Em seguida pretende-se guardar esse nome num ficheiro com o nome “texto.txt”.
with open("texto", "w", encoding="utf-8") as f:
    f.write(nome)
#Se o ficheiro “texto.txt” já existir, deverá removê-lo e criá-lo de novo sem dados.

##################################################
#Crie 2 ficheiros de texto com algo escrito em ambos.

#Desenvolva um programa que solicite o nome dos 2 ficheiros ao utilizador.

#Crie a função junta_fich() que recebe os 2 nomes como argumentos.

#A função deverá criar o ficheiro de saída com a concatenação dos 2 ficheiros.

#O nome do ficheiro de saída deverá ser solicitado ao utilizador.

#Crie 2 ficheiros de texto com algo escrito em ambos.

"""Desenvolva um programa que solicite o nome dos 2 ficheiros ao utilizador.
Crie a função junta_fich() que recebe os 2 nomes como argumentos.
A função deverá criar o ficheiro de saída com a concatenação dos 2 ficheiros. O
nome do ficheiro de saída deverá ser solicitado ao utilizador.
"""
