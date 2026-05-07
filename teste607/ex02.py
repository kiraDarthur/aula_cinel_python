produto = {"nome":"Rato","preco":15.99}
lista_dados2 = []
for items,valor in produto.items():
    lista_dados2["stock"] = 20
    dados1 = items.strip().split(":")
    valor = str(valor)
    dados2 = valor.split(":")
    lista_dados2.append(dados2)

    print(lista_dados2)


preco = lista_dados2[1]
print(f"O preço é {preco}")
preco = 12.50
print(f"O novo valor é {preco}")

