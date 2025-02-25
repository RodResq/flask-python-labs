from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    jogos = ['Tetris', 'Skyrim', 'Crash']
    return render_template('lista.html', titulo='Jogos', lista=jogos)

if __name__ == '__main__':
    app.run(debug=True)