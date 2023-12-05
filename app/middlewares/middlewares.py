from flask import request, jsonify

def validate_json():
    if request.method in ['POST', 'PUT']:
        if not request.is_json:
            return jsonify({'error': 'Request body must be in JSON format', 'status_code': 400})

def validate_fields():
    if request.method == 'POST':
        required_fields = ['nombre', 'descripcion', 'img']
        if not all(field in request.form for field in required_fields):
            return jsonify({'error': 'Required fields are missing', 'status_code': 400})

def validate_data_types():
    if request.method in ['POST', 'PUT']:
        data_types = {'nombre': str, 'descripcion': str, 'img': 'file'}
        for field, data_type in data_types.items():
            if field in request.form and not isinstance(request.form[field], data_type):
                return jsonify({'error': f'Invalid data type for {field}', 'status_code': 400})

def handle_exception(error):
    return jsonify({'error': str(error), 'status_code': 500})

def not_found(error):
    return jsonify({'error': 'Resource not found', 'status_code': 404})
