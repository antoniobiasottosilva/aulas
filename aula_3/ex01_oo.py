class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = produto("detergente", 10.00)
produto2 = produto("carro", 20000.00)

print(produto1.nome)
print(produto1.preco)
print(produto2.nome)
print(produto2.preco)
