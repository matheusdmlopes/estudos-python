qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor > 0:
    qtd += 1
    soma += valor
    valor = float(input("Digite um valor: "))

media = soma / qtd

print(f"A média dos valores digitados é {media:.2f}")
print(f"A soma dos valores digitados é {soma}")
print(f"A quantidade de valores digitados é {qtd}")
