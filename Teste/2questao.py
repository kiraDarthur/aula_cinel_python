"""
notas
"""
# nome e nota do aluno
nome = input("Digite seu nome :")
nota =  int(input(f"{nome.upper()} digite sua nota de 0 a 100 "))

if nota <= 49:
    print(f"{nome} sua nota foi {nota} e sua classificação é : «INSUFICIENTE»")
elif nota >50 or nota < 75:
    print(f"{nome} sua nota foi {nota} e sua classificação é : «BOM»")
else:
    print(f"{nome} sua nota foi {nota} e sua classificação é : «MUITO BOM»")