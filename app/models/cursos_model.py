# Importa la función get_db del módulo db
from app.db import get_db
from flask import current_app as app

def obtener_cursos():
    try:
        # Intenta obtener cursos de la base de datos
        with get_db().cursor() as cursor:
            sql = "SELECT * FROM curso"
            cursor.execute(sql)
            datos = cursor.fetchall()

            # Construye la lista de cursos con la información obtenida de la base de datos
            cursos = [{'codigo': fila[0], 'nombre': fila[1], 'descripcion': fila[2], 'img': fila[3]} for fila in datos]

        # Devuelve un diccionario con la lista de cursos, un mensaje y la cantidad de cursos
        return {'cursos': cursos, 'mensaje': 'Cursos listados', 'count': len(cursos)}

    except Exception as ex:
        # En caso de error, registra el error en los logs y devuelve un diccionario con el error y el código de estado 500
        app.logger.error("Error obteniendo cursos: %s", ex)
        return {'error': str(ex), 'status_code': 500}

def obtener_curso_por_id(id_curso):
    try:
        # Intenta obtener cursos de la base de datos
        with get_db().cursor() as cursor:
            sql = "SELECT * FROM curso WHERE idcurso = {0}".format(id_curso)
            cursor.execute(sql)
            datos = cursor.fetchone()


            if datos == None:
                raise ValueError ('No existen cursos bajo el id numero: {0}'.format(id_curso))
            
                
            # Construye la lista de cursos con la información obtenida de la base de datos
            curso = {'codigo': datos[0], 'nombre': datos[1], 'descripcion': datos[2], 'img': datos[3]}

        # Devuelve un diccionario con la lista de cursos, un mensaje y la cantidad de cursos
        return {'curso': curso, 'mensaje': 'Detalle del curso'}

    except ValueError as er:
        return {'error': str(er), 'status_code': 404}
    except Exception as ex:
        # En caso de error, registra el error en los logs y devuelve un diccionario con el error y el código de estado 500
        app.logger.error("Error obteniendo cursos: %s", ex)
        return {'error': str(ex), 'status_code': 500}

def registrar_curso(nombre, descripcion, img_url):
    try:
       with get_db().cursor() as cursor:
            sql = '''INSERT INTO curso (nombre, descripcion, img)
                     VALUES('{0}', '{1}', '{2}')'''.format(nombre, descripcion, img_url)
            cursor.execute(sql)

            get_db().commit()

            return {'mensaje': 'Curso registrado'}
 
    except Exception as ex:
        app.logger.error("Error registrando curso: %s", ex)
        return {'error': str(ex), 'status_code': 500}

# Le asigno None a img para que en caso de no venir desde el front, no me de error la funcion
def actualizar_curso(id_curso, nombre, descripcion, img=None):
    try:
        with get_db().cursor() as cursor:
            # Verifica si se proporcionó una nueva imagen
            if img:

            # Si la subida de la imagen fue exitosa, actualiza el registro en la base de datos
                sql = '''UPDATE curso SET nombre = '{0}', descripcion = '{1}', img = '{2}'
                            WHERE idcurso = '{3}' '''.format(nombre, descripcion, img, id_curso)
                cursor.execute(sql)
                
            else:
                # Si no se proporciona una nueva imagen, actualiza solo el nombre y la descripción
                sql = '''UPDATE curso SET nombre = '{0}', descripcion = '{1}'
                         WHERE idcurso = '{2}' '''.format(nombre, descripcion, id_curso)
                cursor.execute(sql)

            get_db().commit()

            return {'mensaje': 'Curso actualizado'}

    except Exception as ex:
        app.logger.error("Error actualizando curso: %s", ex)
        return {'error': str(ex), 'status_code': 500}

def eliminar_curso(id_curso):
    try:
       with get_db().cursor() as cursor:
            sql = "DELETE FROM curso WHERE idcurso = '{0}'".format(id_curso)
            cursor.execute(sql)

            get_db().commit()

            return {'mensaje': 'Curso eliminado'}

    except Exception as ex:
        # En caso de error, registra el error en los logs y devuelve un diccionario con el error y el código de estado 500
        app.logger.error("Error eliminando curso: %s", ex)
        return {'error': str(ex), 'status_code': 500}
