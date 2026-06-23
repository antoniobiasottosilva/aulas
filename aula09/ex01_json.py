from flask import Flask, jsonify

app = Flask(__name__)

produto = [
    {"id": 1, "nome": "jorge", "preco": 99.99, "disponivel": "true"},
]

@app.route("/produto")
def listar_produto():
    return jsonify(produto)

if __name__ == "__main__":
    app.run(debug=True)
