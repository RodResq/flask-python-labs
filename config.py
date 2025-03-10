SECRET_KEY = 'app_jogoteca'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '123',
        servidor = 'localhost',
        database = 'jogoteca'
    )
 