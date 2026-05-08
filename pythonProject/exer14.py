"""escreva uma funçao que dado um numero n , verifique se este e triangular.
Um numero n diz triangular se existir um outro numero , m, menor que n ta que n= 1+2+3+... m.
 A funçao devera devolver true se n é tringular e false caso contrario."""
def triangular(num):
    soma = 0
    x =1
    while soma < num:
        # att aa soma com valor x vale no momento
        soma = soma + x
        x = x + 1
    if soma == num:
        return f"{num} é trinangular"
    return f"{num} não é triangular"

############################################################
num = int(input("insira  1 nº :"))
print(triangular(num))
print(f"valor de x em baixo {x}")