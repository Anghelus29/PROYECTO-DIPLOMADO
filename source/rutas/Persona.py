from flask import Blueprint, jsonify, request

#importar entidad
from modelos.entidades.persona import Persona
#importar modelos
from modelos.PersonaModelo import PersonaModelo

main = Blueprint('persona_blueprint',__name__)

#RUTA PARA VER TODOS LOS USUARIOS
@main.route('/')
def get_personas():
    try:
        personas=PersonaModelo.get_personas()
        return jsonify(personas)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
    
#RUTA PARA VER TODOS UN USUARIO DE ACUERDO A SU CEDULA DE IDENTIDAD
@main.route('/<ci>')
def get_persona(ci):
    try:
        persona=PersonaModelo.get_persona(ci)
        if persona != None:
            return jsonify(persona)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    

#RUTA PARA VER EL PROMEDIO DE EDAD DE ACUERDO A SU CEDULA DE IDENTIDAD
@main.route('/promedio/<ci>')
def get_promedio(ci):
    try:
        persona=PersonaModelo.get_promedio(ci)
        if persona != None:
            return jsonify({'promedio_edad': persona})
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
    
#RUTA PARA VER EL ESTADO
@main.route('/estado')
def get_estado():
    return jsonify({
        'nameSystem':"api-users",
        'version':"0.0.1",
        'developer':"Wilder Rosas Flores",
        'email':"rosasfloreswilder@gmail.com"
    })


#RUTA PARA VER EL INGRESAR NUEVO USUARIO   
@main.route('/add', methods=['POST'])
def anadir_persona():
    try:
        ci=request.json['ci']
        nombre=request.json['nombre']
        primer_apellido=request.json['primer_apellido']
        segundo_apellido=request.json['segundo_apellido']
        fecha_nacimiento=request.json['fecha_nacimiento']

        persona=Persona(ci,nombre,primer_apellido,segundo_apellido,fecha_nacimiento)

        filas_afectadas=PersonaModelo.anadir_persona(persona)

        if filas_afectadas ==1:
            return jsonify({'message': "Usuario Registrado Correctamente"})
        else:
            return jsonify({'message': "Error al insertar datos"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    

#RUTA PARA VER EL ACTUALIZAR DATOS DEL USUARIO
@main.route('/update/<ci>', methods=['PUT'])
def modificar_persona(ci):
    try:
        ci=request.json['ci']
        nombre=request.json['nombre']
        primer_apellido=request.json['primer_apellido']
        segundo_apellido=request.json['segundo_apellido']
        fecha_nacimiento=request.json['fecha_nacimiento']

        persona=Persona(ci,nombre,primer_apellido,segundo_apellido,fecha_nacimiento)

        filas_afectadas=PersonaModelo.modificar_persona(persona)

        if filas_afectadas ==1:
            return jsonify({'message': "Usuario Modificado Correctamente"})
        else:
            return jsonify({'message': "Error al modificar datos"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
    
#RUTA PARA ELIMINAR UN USUARIO DE ACUERDO A SU CEDULA DE IDENTIDAD
@main.route('/delete/<ci>', methods=['DELETE'])
def eliminar_persona(ci):
    try:
        persona=Persona(ci)

        filas_afectadas=PersonaModelo.eliminar_persona(persona)

        if filas_afectadas ==1:
            return jsonify({'message': "Usuario Eliminado Correctamente"})
        else:
            return jsonify({'message': "No se elimino ningun usuario"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
