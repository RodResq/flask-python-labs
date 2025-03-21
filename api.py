from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import urlencode
from flask_wtf.csrf import CSRFProtect

        
app = Flask(__name__)


db = SQLAlchemy()
app.config.from_pyfile('config.py')

csrf = CSRFProtect(app)
  
db.init_app(app)

from views import *    


if __name__ == '__main__':
    app.run(debug=True)