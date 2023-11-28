from flask import jsonify, request

def validate_json():
    if request.method in ['POST', 'PUT']:
        if not request.is_json:
            return jsonify({'error': 'La solicitud debe ser de tipo JSON'}), 400

def validate_fields():
    if request.method in ['POST', 'PUT']:
        required_fields = ['nombre', 'descripcion', 'img']
        if not all(field in request.json for field in required_fields):
            return jsonify({'error': 'Los campos nombre, descripcion e img son obligatorios'}), 400

def validate_data_types():
    if request.method in ['POST', 'PUT']:
        if not isinstance(request.json.get('nombre'), str) or not isinstance(request.json.get('descripcion'), str) or not isinstance(request.json.get('img'), str):
            return jsonify({'error': 'Los tipos de datos de los campos son incorrectos'}), 400

def handle_exception(error):
    return jsonify({'error': 'Error en la solicitud'}), 500

def not_found(error):
    return jsonify({'error': 'Recurso no encontrado'}), 404