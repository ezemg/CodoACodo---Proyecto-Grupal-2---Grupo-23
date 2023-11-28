# Importa funciones y objetos necesarios de Flask, db y cursos_model
from flask import Blueprint, jsonify, request
from models.cursos_model import obtener_cursos, registrar_curso, actualizar_curso, eliminar_curso
from middlewares.middlewares import (
    validate_json,
    validate_fields,
    validate_data_types,
    handle_exception,
    not_found)
    
# Crea un objeto Blueprint llamado curso_routes
cursos_routes = Blueprint('curso_routes', __name__)

# Middlewares
cursos_routes.before_request(validate_json)
cursos_routes.before_request(validate_fields)
cursos_routes.before_request(validate_data_types)
cursos_routes.errorhandler(Exception)(handle_exception)
cursos_routes.errorhandler(404)(not_found)

# Define una ruta para obtener cursos
@cursos_routes.route('/cursos', methods=['GET'])
def obtener_cursos_route():
    # Llama a la función obtener_cursos y obtiene la respuesta
    response = obtener_cursos()
    # Devuelve la respuesta como JSON
    return jsonify(response)

# Define una ruta para registrar un curso
@cursos_routes.route('/cursos', methods=['POST'])
def registrar_curso_route():
    # Obtiene nombre y créditos desde la solicitud JSON
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    img = request.json['img']
    # Llama a la función registrar_curso y obtiene la respuesta
    response = registrar_curso(nombre, descripcion, img)
    # Devuelve la respuesta como JSON
    return jsonify(response)

# Define una ruta para actualizar un curso
@cursos_routes.route('/cursos/<int:id_curso>', methods=['PUT'])
def actualizar_curso_route(id_curso):
    # Obtiene nombre y créditos desde la solicitud JSON
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    img = request.json['img']

    # Llama a la función actualizar_curso y obtiene la respuesta
    response = actualizar_curso(id_curso, nombre, descripcion, img)
    # Devuelve la respuesta como JSON
    return jsonify(response)

# Define una ruta para eliminar un curso
@cursos_routes.route('/cursos/<int:id_curso>', methods=['DELETE'])
def eliminar_curso_route(id_curso):
    # Llama a la función eliminar_curso y obtiene la respuesta
    response = eliminar_curso(id_curso)
    # Devuelve la respuesta como JSON
    return jsonify(response)
