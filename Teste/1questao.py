"""
preço/descontoo
"""
preco = int(input("Qual preço da roupa?"))
desconto = float(input("Qual valor do desconto ? "))
formula_desconto = preco * desconto
print(f"O valor  a pagar  são de €{preco - formula_desconto}")
