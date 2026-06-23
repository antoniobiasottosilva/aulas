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

if __name__ == "__main__":
    app.run(debug=True)
