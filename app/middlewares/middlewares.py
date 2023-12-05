from flask import jsonify

def not_found(error):
    return jsonify({'error': 'Resource not found', 'status_code': 404})