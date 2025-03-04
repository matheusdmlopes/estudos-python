class Main:
    pass


print("Testando o projeto.")

from cliente import Cliente

from conta import Conta

cliente1 = Cliente("João", "1234-5678")
conta = Conta("123-4", cliente1.nome, 120.0, 1000.0)

print("Nome do cliente: ", conta.titular)
print("Saldo do cliente: ", conta.saldo)
print("Limite do cliente: ", conta.limite)
print("Número da conta: ", conta.numero)
