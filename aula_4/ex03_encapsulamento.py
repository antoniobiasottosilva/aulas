class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Erro: valor de deposito deve ser positivo")

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: valor de saque deve ser positivo")
        elif valor > self.__saldo:
            print("Erro: saldo insuficiente")
        else:
            self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo

    def extrato(self):
        print(f"Titular: {self.__titular} | Saldo: R$ {self.__saldo:.2f}")


conta1 = ContaBancaria("Mariana")
conta1.extrato()

conta1.depositar(500)
conta1.extrato()

conta1.sacar(150)
conta1.extrato()

conta1.sacar(1000)
conta1.depositar(-50)

print(conta1.get_saldo())
