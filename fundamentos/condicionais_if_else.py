notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

mediaFinal = (notaA + notaB) / 2

if mediaFinal >= 7.0:
    print("Parabéns! Você foi aprovado. Sua média é %.2f" % mediaFinal)
else:
    print("Você foi reprovado. Sua média é %.2f" % mediaFinal)
