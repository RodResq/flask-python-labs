import os
from api import app

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['PATH_UPLOADS']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
    return 'capa_padrao.jpg'
        
        
def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['PATH_UPLOADS'], arquivo))