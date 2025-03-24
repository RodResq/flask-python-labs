from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from models import Jogos
from api import app, db
from helpers import recupera_imagem, deleta_arquivo, FormularioJogo
import time


@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Jogos', lista=lista)


@app.route("/novo")
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioJogo(request.form)
    
    return render_template('novo.html', titulo='Novo Jogo', form=form)


@app.route("/criar", methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    jogo = Jogos.query.filter_by(nome=nome).first()
    
    if jogo:
        flash('Jogo já existente!')
        return redirect(url_for('index'))
    
    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()
    
    arquivo = request.files['arquivo']
    path_uploads = app.config['PATH_UPLOADS']
    timestamp = time.time()
    
    arquivo.save(f'{path_uploads}/capa{novo_jogo.id}-{timestamp}.jpg')
    
    return redirect(url_for('index'))


@app.route("/editar/<int:id>")
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    jogo = Jogos.query.filter_by(id=id).first()
    
    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console
    
    capa_jogo = recupera_imagem(id)
    
    return render_template('editar.html', titulo='Editar Jogo', id=id, form=form, capa_jogo=capa_jogo)


@app.route("/atualizar", methods=['POST',])
def atualizar():
    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    form = FormularioJogo(request.form)
    
    if form.validate_on_submit():
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data
        
        db.session.add(jogo)
        db.session.commit()
        
        arquivo = request.files['arquivo']
        path_uploads = app.config['PATH_UPLOADS']
        timestamp = time.time()
        
        deleta_arquivo(jogo.id)
        
        arquivo.save(f'{path_uploads}/capa{jogo.id}-{timestamp}.jpg')
    
    return redirect(url_for('index'))

@app.route("/deletar/<int:id>")
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    
    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso!')
    
    return redirect(url_for('index'))   


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)