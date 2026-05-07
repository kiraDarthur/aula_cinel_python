
soma= 0
maior = 0
lista = []
with open("numeros.txt", "r") as fp:
    for linha in fp:
        lista.append(linha.strip())
    for x in lista:
        x = int(x)
        soma = soma + x
        if  maior < x:
            maior = x
        tamanho = len(lista)


print(f"A soma dos numeros é:  {soma}")
print(f"O maior número é : {maior}")
media = soma/tamanho
print(f"A média dos numeros são: {media:.2f}")
#print(soma)