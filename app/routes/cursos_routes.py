# Importa funciones y objetos necesarios de Flask, db y cursos_model
from flask import Blueprint, jsonify, request, current_app as app

from app.controllers.image_controller import subir_imagen
from app.models.cursos_model import (
    obtener_cursos, 
    registrar_curso, 
    actualizar_curso, 
    eliminar_curso, 
    obtener_curso_por_id
    )


# Crea un objeto Blueprint llamado curso_routes para poder acceder desde archivo app y que las rutas queden registradas
cursos_routes = Blueprint('curso_routes', __name__)


# Defino ruta para listar todos los cursos
@cursos_routes.route('/cursos', methods=['GET'])
def obtener_cursos_route():
    # Llama a la función obtener_cursos y obtiene la respuesta
    response = obtener_cursos()
    # Devuelve la respuesta como JSON
    return jsonify(response)

# Defino ruta para ver un solo curso
@cursos_routes.route('/cursos/<int:id_curso>', methods=['GET'])
def obtener_curso_por_id_route(id_curso):
    response = obtener_curso_por_id(id_curso)

    if 'error' in response:
        print(response)
        return jsonify(response), response.get('status_code', 500)
    else:

        return jsonify(response)

# Defino ruta para crear nuevo curso
@cursos_routes.route('/cursos', methods=['POST'])
def registrar_curso_route():
    # Obtiene otros datos desde el formulario
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    # Maneja el archivo de imagen

    img = request.files.get('img')  # Usa get para manejar el caso en que 'img' no está presente

    img_public_url = None

    if img:
        # Llamo al controlador para que suba la imagen y me retorne la URL del hosting
        img_public_url = subir_imagen(img)

    # Llama a la función registrar_curso del modelo para guardar en db
    response = registrar_curso(nombre, descripcion, img_public_url)

    # Devuelve la respuesta como JSON
    return jsonify(response)

# Define una ruta para actualizar un curso
@cursos_routes.route('/cursos/<int:id_curso>', methods=['PUT'])
def actualizar_curso_route(id_curso):
    # Obtiene nombre y créditos desde la solicitud JSON
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    img = request.files.get('img')  # Usa get para manejar el caso en que 'img' no está presente
    img_public_url = None

    # Si hay imagen, subo la nueva imagen a cloudinary y guardo en la db
    if img:
        img_public_url = subir_imagen(img)

        response = actualizar_curso(id_curso, nombre, descripcion, img_public_url)
    # Si no hay imagen, guardo en la db nombre y descripcion
    else:
        response = actualizar_curso(id_curso, nombre, descripcion)

    # Devuelve la respuesta como JSON
    return jsonify(response)

# Define una ruta para eliminar un curso
@cursos_routes.route('/cursos/<int:id_curso>', methods=['DELETE'])
def eliminar_curso_route(id_curso):
    # Llama a la función eliminar_curso y obtiene la respuesta
    response = eliminar_curso(id_curso)
    # Devuelve la respuesta como JSON
    return jsonify(response)
