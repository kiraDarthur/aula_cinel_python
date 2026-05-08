frase = input("escreva uma frase ")
i = 0
for letra in frase:
    if letra != " ":
        i = i + 1

print(f"Esta frase tem  {i} letras ")
#############################
m = 0
for letra in frase:
    if letra != letra.isupper():
        m = m + 1
print(f"Esta frase tem {m} maiusculas ")