from flask import Flask,render_template
from funcoesloteria import *

app = Flask(__name__)
# route -> pythonloteria.com/
# função -> website onde o usuário tem três opções de jogos de loteria para escolher
# e são: lotofácil, quina e mega sena.
# template.

@app.route("/")
def homepage():
    return render_template ("index.html")

@app.route('/loto', methods=['POST','GET'])
def lotofacil():
    jogo_lotofacil = lista_loto_facil()
    return render_template("index.html", jogo_lotofacil=jogo_lotofacil)
@app.route('/quina', methods=['POST','GET'])
def quina():
    jogo_quina = lista_quina()
    return render_template("index.html", jogo_quina=jogo_quina)
@app.route('/sena', methods=['POST','GET'])
def megasena():
    jogo_megasena = lista_mega_sena()
    return render_template("index.html", jogo_megasena=jogo_megasena)

@app.route('/style.css')
def style():
    return app.send_static_file("style.css")

@app.route('/imagemfundo.jpg')
def imagemfundo():
    return app.send_static_file("index.html")



#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
