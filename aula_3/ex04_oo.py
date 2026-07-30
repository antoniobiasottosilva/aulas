class contabancaria:
    def __init__(self, titular, saldo=200.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("saldo insuficiente")

    def extrato(self):
        print(f"Titular: {self.titular}")
        print(f"saldo: {self.saldo}")

conta = contabancaria("Eu")
conta.extrato()
conta.depositar(50)
conta.extrato()
conta.sacar(200)
conta.extrato()