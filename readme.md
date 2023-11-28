1) Instalar dependencias de la lista a continuacion mediante pip install

blinker
click  
colorama
Flask
Flask-Cors
itsdangerous
Jinja2
MarkupSafe
marshmallow
mysql-connector-python
packaging
protobuf
python-dotenv
Werkzeug

2) Crear la base de datos para poder trabajar localmente (ejecutar script schema.sql)

3) Generar un archivo que se llame '.env' en la raíz del proyecto con las siguientes variables:

DB_HOST='host de la DB' en general es localhost
DB_USER='usuario de la db' por defecto es root
DB_PASSWORD='password de la db' password que hayan elegido, en caso de no tener password avisarme y modificamos dos lineas de codigo
DB_DATABASE='codoacodo' es el nombre que le di a la db en el script.
DB_PORT='puerto en el que este la db' por defecto es el 3306.
FLASK_ENV= 'development' o'production' usar por defecto el valor 'development'. 'production' es solamente para el proyecto que esté subido a un hosting. Si usan 'production' las solicitudes a la API van a caer directo a la db que está online. 

Este archivo es para que cada uno pueda poner sus credenciales de acceso a la base de datos y no tener que estar modificando el codigo fuente.

4) Los endpoints de la api de desarrollo son

GET     http://127.0.0.1:5000/cursos          -- Para listar todos los cursos
POST    http://127.0.0.1:5000/cursos          -- Para crear un nuevo cursos
PUT     http://127.0.0.1:5000/cursos/idcurso  -- Para modificar un curso existente (reemplazar idcurso por numero de id en la db)
DELETE  http://127.0.0.1:5000/cursos/idcurso  -- Para eliminar un curso existente (reemplazar idcurso por numero de id en la db)

5) Para correr la app, desde la raiz del proyecto, ejecutar:

python -m app.app