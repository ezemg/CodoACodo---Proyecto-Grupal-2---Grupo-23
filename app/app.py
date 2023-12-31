# app/app.py
from flask import Flask, g
from flask_cors import CORS

# importaciones modulos propios
from app.routes.cursos_routes import cursos_routes
from app.config import get_config
from app.db import close_db, get_db
from app.middlewares.middlewares import not_found

app = Flask(__name__)
CORS(app)
app.config.from_object(get_config())


app.register_blueprint(cursos_routes)
app.register_error_handler(404, not_found)

# Registrar las rutas
@app.before_request
def before_request():
    g.db = get_db()

@app.teardown_request
def teardown_request(exception=None):
    close_db(exception)




if __name__ == '__main__':
    # app.config.from_object(get_config())
    # app.register_blueprint(cursos_routes)
    app.register_error_handler(404, not_found)
    # print(f"Modo de depuración: {app.debug}") 
    app.run()