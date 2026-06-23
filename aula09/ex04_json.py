from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "jorge", "preco": 99.99, "disponivel": True},
     {"id": 2, "nome": "arroz", "preco": 199.99, "disponivel": True},
      {"id": 3, "nome": "carro", "preco": 929.99, "disponivel": True},
       {"id": 4, "nome": "mamao", "preco": 999.99, "disponivel": False},
]

@app.route("/produtos")
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos/disponiveis")
def produtos_disponiveis():
    disponiveis = []
    
    for produto in produtos:
        if produto["disponivel"] == True:
            disponiveis.append(produto)

    return jsonify(disponiveis)


if __name__ == "__main__":
    app.run(debug=True)
