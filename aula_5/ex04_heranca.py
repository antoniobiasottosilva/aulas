class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(f"Aluno | Nome: {self.nome} | Idade: {self.idade} | Matricula: {self.matricula}")


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(f"Professor | Nome: {self.nome} | Idade: {self.idade} | Salario: R$ {self.salario:.2f}")


pessoas = [
    Aluno("Ana", 17, 12345),
    Professor("Carlos", 40, 4500.00)
]

for pessoa in pessoas:
    pessoa.apresentar()
