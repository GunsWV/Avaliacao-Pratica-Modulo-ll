from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/soma")
def soma():
    try:
        v1 = float(request.args.get("valor1", 0))
        v2 = float(request.args.get("valor2", 0))
        return {"resultado": v1 + v2}
    except ValueError:
        return {"erro": "Parâmetros inválidos"}

@app.route("/subtrair")
def subtrair():
    try:
        v1 = float(request.args.get("valor1", 0))
        v2 = float(request.args.get("valor2", 0))
        return {"resultado": v1 - v2}
    except ValueError:
        return {"erro": "Parâmetros inválidos"}

@app.route("/multiplicar")
def multiplicar():
    try:
        v1 = float(request.args.get("valor1", 0))
        v2 = float(request.args.get("valor2", 0))
        return {"resultado": v1 * v2}
    except ValueError:
        return {"erro": "Parâmetros inválidos"}

@app.route("/dividir")
def dividir():
    try:
        v1 = float(request.args.get("valor1", 0))
        v2 = float(request.args.get("valor2", 0))
        if v2 == 0:
            return {"erro": "Divisão por zero não é permitida"}
        return {"resultado": v1 / v2}
    except ValueError:
        return {"erro": "Parâmetros inválidos"}

if __name__ == "__main__":
    app.run(debug=True)    