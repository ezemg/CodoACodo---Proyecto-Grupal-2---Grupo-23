import os
import cloudinary
from flask import current_app as app
from cloudinary.uploader import upload

cloudinary.config(
        cloud_name=os.environ.get('CLOUD_NAME'),
        api_key=os.environ.get('API_KEY'),
        api_secret=os.environ.get('API_SECRET')
    )

def subir_imagen(img):
    try:
        response = upload(img, folder='cursos')
        return response.get('secure_url')
    except Exception as e:
        print(f"Error al subir la imagen a Cloudinary: {e}")
        return None