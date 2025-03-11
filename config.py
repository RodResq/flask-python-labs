import os

SECRET_KEY = 'app_jogoteca'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'New_Strong_Pass123!',
        servidor = 'localhost',
        database = 'jogoteca'
    )
 
PATH_UPLOADS = os.path.dirname(os.path.abspath(__file__))  