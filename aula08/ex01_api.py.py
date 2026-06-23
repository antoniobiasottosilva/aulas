from flask import Flask
app = Flask(__name__)
@app.route("/")
def inicio():
    return "Pagina inicial da API"
@app.route("/nome")
def aluno():
    return "Antonio Carlos Biasotto da Silva"

if __name__ == "__main__":
    app.run(debug=True)
