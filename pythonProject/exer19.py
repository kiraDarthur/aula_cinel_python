"""
crie programa que leia o nome completo de um ultilizador e mostre
1 nome com todas as letras maisculas
2 nomes com todas minusculas
3 quantas letras tem o nome sem os espaços
4 quantas ltras tem o 1 nome

"""

nome_ult = input("digite seu nome completo")
#1
nome_mais =  nome_ult.upper()
#2
nome_minus = nome_ult. lower()
#3
i = 0
for letra in nome_ult:
    if letra != " " :
        i = i + 1

print(i)