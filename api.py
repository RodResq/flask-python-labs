from flask import Flask, render_template, request, redirect


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
jogo1 = Jogo('Tetris', 'Skyrim', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNS')

jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', lista=jogos)


@app.route("/novo")
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route("/criar", methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)
    
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)