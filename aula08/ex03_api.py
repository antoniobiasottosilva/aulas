from flask import Flask
app = Flask(__name__)
@app.route("/")
def inicio():
    return "Bem-vindo"
@app.route("/saudacao")
def saudacao():
    return "seja muito bem vindo"
@app.route("/data")
def data():
    from datetime import date
    return str(date.today())

if __name__ == "__main__":
    app.run(debug=True)
