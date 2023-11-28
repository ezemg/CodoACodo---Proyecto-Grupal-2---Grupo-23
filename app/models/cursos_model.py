# Importa la función get_db del módulo db
from db import get_db

def obtener_cursos():
    try:
        from app import app  # Importa el objeto app localmente para evitar círculos de importación

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

def registrar_curso(nombre, descripcion, img):
    try:
       from app import app
       with get_db().cursor() as cursor:
            sql = '''INSERT INTO curso (nombre, descripcion, img)
                     VALUES('{0}', '{1}', '{2}')'''.format(nombre, descripcion, img)
            cursor.execute(sql)

            get_db().commit()

            return {'mensaje': 'Curso registrado'}

    except Exception as ex:
        app.logger.error("Error registrando curso: %s", ex)
        return {'error': str(ex), 'status_code': 500}

def actualizar_curso(id_curso, nombre, descripcion, img):
    try:
       from app import app
       with get_db().cursor() as cursor:
            sql = '''UPDATE curso SET nombre = '{0}', descripcion = '{1}', img '{2}'
                     WHERE idcurso = '{3}' '''.format(nombre, descripcion, img, id_curso)
            cursor.execute(sql)

            get_db().commit()

            return {'mensaje': 'Curso actualizado'}

    except Exception as ex:
        app.logger.error("Error actualizando curso: %s", ex)
        return {'error': str(ex), 'status_code': 500}

def eliminar_curso(id_curso):
    try:
       from app import app
       with get_db().cursor() as cursor:
            sql = "DELETE FROM curso WHERE idcurso = '{0}'".format(id_curso)
            cursor.execute(sql)

            get_db().commit()

            return {'mensaje': 'Curso eliminado'}

    except Exception as ex:
        # En caso de error, registra el error en los logs y devuelve un diccionario con el error y el código de estado 500
        app.logger.error("Error eliminando curso: %s", ex)
        return {'error': str(ex), 'status_code': 500}
