class Main:
    pass


from cliente import Cliente

from conta import Conta

cliente1 = Cliente("João", "1234-5678")
conta = Conta("123-4", cliente1.get_nome())

conta.deposito(100.0)
conta.saque(50.0)
conta.extrato()
