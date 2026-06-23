from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "jorge", "preco": 99.99, "disponivel": "true"},
     {"id": 2, "nome": "arroz", "preco": 199.99, "disponivel": "true"},
      {"id": 3, "nome": "carro", "preco": 929.99, "disponivel": "true"},
       {"id": 4, "nome": "mamao", "preco": 999.99, "disponivel": "true"},
]

@app.route("/produtos")
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos/<int:id>")
def buscar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
        
    return jsonify({"erro": "produto nao encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
