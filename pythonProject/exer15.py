"""potencia"""
def pot(b,e):
    if e == 0:
        return 1
    valor = b * pot(b, e-1)
    return valor

##########################################
base  = int(input("insira a base : "))
exp = int(input("insira o  expoente : "))
resp = pot(base,exp)
print(f"pot({base},{exp}) = {resp}") #(3,2)=9