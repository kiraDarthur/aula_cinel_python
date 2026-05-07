def vogais(palavra):
    i = 0
    vogais ="a,e,i,o,u"
    for x in palavra.lower() : # TRANSFORMA a palavra em minusculo
        if x in vogais:
            i = i + 1
    return i
######################
palavra = ("Arthur gOstA de carro")
print(f"A palavra {palavra} tem {vogais(palavra)} .")