"""
media valores
programaque tem 5 valores  de 0 a 20  caa valor lido  programa
guarda em tupla  o programa  devera determinar meedia arredondada a uma casa decimal  ,
 usar o funçao round
"""
n = 0
lista = ()
lista =list(lista)
while n < 5:
    n +=1
    valor = int(input(f"Digite {n}º valor entre  « 0 a 20 » "))
    lista.append(valor)
    soma = sum(lista)
    media = soma / 5
print(f"A medida é {round(media,3)}")

