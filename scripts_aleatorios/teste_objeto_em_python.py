class Pessoa:
    "Isto é uma classe nova chamada Pessoa, e isso é a docstring da classe, traduzida em __doc__."

    idade = 15

    def saudacao(self):
        return "Olá, eu sou uma pessoa!"


matheus = Pessoa()

print(matheus.idade)
print(matheus.saudacao)
print(matheus.saudacao())
matheus.saudacao()
print(Pessoa.saudacao(matheus))
print(matheus.__doc__)
