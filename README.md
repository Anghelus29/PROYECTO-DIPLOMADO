Primeramente crear la base de datos en POSTGRESQL

create database dbapirest

Luego crear la tabla con los siguientes campos

Create table persona
(
	ci varchar (10),
	nombre varchar(100),
	primer_apellido varchar(200),
	segundo_apellido varchar(200),
	fecha_nacimiento date
)
LUEGO UNA VEZ DESCARGADO EL PROGRAMA DEBEMOS INSTALAR EL ENTORNO VIRTUAL PARA CREAR EL ARCHIVO env ESTO LO HACEMOS DESDE LA TERMINAL CON EL SIGUIENTE COMANDO

python -m virtualenv env

LUEGO DEBEMOS ACTIVAR EL ENTORNO VIRTUAL CON EL SIGUIENTE COMANDO (OJO TOMAR EN CUENTA QUE  SU WINDOWS POWERSHELL DEBE PODER EJECUTAR SCRIPTS)

.\env\Scripts\activate

LUEGO INSTALAMOS FLASK Y LOS PAQUETES QUE SE UTILIZARON PARA EL PROYECTO CON EL SIGUIENTE COMANDO

pip install flask flask-cors psycopg2 python-decouple python-dotenv

Luego en el archivo .env colocar los datos para la conexion a la base de datos

SECRET_KEY = ANGHELUS   ------------> ingresar cualquier clave secreta
HOST = localhost         -------------> comunmente el host seimpre suele ser localhost
USER = postgres           -------------> por lo general el user es postgres          
PASSWORD = anghelus2299   -------------> ingresar la contrasena que tiene su postgresql
DATABASE= dbapirest        -------------> ingresar el nombre de la base de datos para el programa es dbapirest 

EL COMANDO PARA HACER CORRER EL PROGRAMA ES EL SIGUIENTE

python .\source\app.py

PARA VERIFICAR LAS RUTAS SE PUEDE USAR EL PROGRAMA INSOMNIA O CUALQUIER OTRO DE SU PREFERENCIA


RUTAS LAS PARA EL GET, PUT, DELETE Y POST


Al hacer correr el proyecto por defecto el servidor tendra el siguiente puerto
http://localhost:5000 ------------> esto puede variar


--------------------------------------------------------------------------------------------

La ruta para mostrar todos los usuarios es: METODO GET 
http://localhost:5000/api/persona/

--------------------------------------------------------------------------------------------

La ruta para mostrar UN SOLO usuario es: METODO GET 
http://localhost:5000/api/persona/<ci>     --------> en ci ingresar la cedula de identidad a mostrar

--------------------------------------------------------------------------------------------

La ruta para adicionar un usuario es: METODO POST 
http://localhost:5000/api/persona/add

OJO LOS CAMPOS NO ESTAN VALIDADOS LOS DATOS TIENEN QUE ESCRIBIRSE CORRECTAMENTE COMO EN EL EJEMPLO QUE SE MUESTRA
Y LA CEDULA DE IDENTIDAD NO ESTA EN FORMATO SERIAL SI REGISTRA OTRO USUARIO CON EL MISMO CI HABRA CONFLICTO

la fecha tiene que ir en este formato = 1999-02-22

ejemplo en el JSON
{
	"ci":"1",
	"nombre":"Wilder",
	"primer_apellido":"Rosas",
	"segundo_apellido":"Flores",
	"fecha_nacimiento":"1999-02-22"
}

--------------------------------------------------------------------------------------------


La ruta para modificar un usuario es: METODO PUT 
http://localhost:5000/api/persona/update/ci     --------> en ci ingresar la cedula de identidad del usuario a modificar

OJO LOS CAMPOS NO ESTAN VALIDADOS LOS DATOS TIENEN QUE ESCRIBIRSE CORRECTAMENTE COMO EN EL EJEMPLO QUE SE MUESTRA

la fecha tiene que ir en este formato = 1999-02-22

ejemplo en el JSON
{
	"ci":"3",
	"nombre":"NUEVO DATO",
	"primer_apellido":"NUEVO DATO",
	"segundo_apellido":"NUEVO DATO",
	"fecha_nacimiento":"NUEVO DATO"       
}

--------------------------------------------------------------------------------------------

La ruta para eliminar un usuario es: METODO DELETE
http://localhost:5000/api/persona/delete/ci   -------> en ci ingresar la cedula de identidad del usuario a eliminar

--------------------------------------------------------------------------------------------

La ruta para ver el promedio de edad es: METODO GET
http://localhost:5000/api/persona/promedio/ci   -------> en ci ingresar la cedula de identidad del usuario para ver su promedio de edad

--------------------------------------------------------------------------------------------

La ruta para ver el estado es: METODO GET
http://localhost:5000/api/persona/estado



