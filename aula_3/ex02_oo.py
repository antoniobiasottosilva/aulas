class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco - (self.preco * (percentual / 100))

produto1 = produto("detergente", 10.00)
produto2 = produto("carro", 20000.00)

novo = produto1.desconto(10)

print(novo)