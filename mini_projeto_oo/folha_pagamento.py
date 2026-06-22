class Funcionario:
    def __init__(self, nome, matricula, salario_fixo):
        self.__nome = nome
        self.__matricula = matricula
        self.set_salario_fixo(salario_fixo)

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_salario_fixo(self):
        return self.__salario_fixo

    def set_salario_fixo(self, valor):
        if valor < 0:
            print("Erro: salario fixo nao pode ser negativo")
        else:
            self.__salario_fixo = valor

    def calcular_salario(self):
        return self.__salario_fixo

    def exibir(self):
        print(f"Nome : {self.__nome} | Matricula : {self.__matricula} | Tipo : {type(self).__name__} | Salario : R$ {self.calcular_salario():.2f}")


class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo()


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, total_vendas):
        super().__init__(nome, matricula, salario_fixo)
        self.__total_vendas = total_vendas

    def get_total_vendas(self):
        return self.__total_vendas

    def set_total_vendas(self, valor):
        if valor < 0:
            print("Erro: total de vendas nao pode ser negativo")
        else:
            self.__total_vendas = valor

    def calcular_salario(self):
        comissao = self.__total_vendas * 0.10
        return self.get_salario_fixo() + comissao


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)
        self.__bonus = 1500.00

    def get_bonus(self):
        return self.__bonus

    def calcular_salario(self):
        return self.get_salario_fixo() + self.__bonus


funcionarios = [
    CLT("Ana", "001", 3000.00),
    Vendedor("Jorge", "002", 2000.00, 12000.00),
    Gerente("CARRO", "003", 5000.00),
]

for func in funcionarios:
    func.exibir()
