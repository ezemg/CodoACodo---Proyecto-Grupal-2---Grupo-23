# app/app.py
from flask import Flask, g
from flask_cors import CORS
from routes.cursos_routes import cursos_routes
from config import get_config
from db import close_db, get_db
from middlewares.middlewares import not_found

app = Flask(__name__)
CORS(app)

# Registrar las rutas
@app.before_request
def before_request():
    g.db = get_db()

@app.teardown_request
def teardown_request(exception=None):
    close_db(exception)

if __name__ == '__main__':
    app.config.from_object(get_config())
    app.register_blueprint(cursos_routes)
    app.register_error_handler(404, not_found)
    app.run()