class Conta:
    def __init__(self, numero, titular):
        self._numero = numero
        self._titular = titular
        self._saldo = 0.0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo não pode ser negativo.")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def deposito(self, valor):
        self._saldo += valor
        print("Depósito realizado com sucesso.")

    def extrato(self):
        print("Saldo: ", self._saldo)
        print("Titular: ", self._titular)
        print("Número da conta: ", self._numero)
