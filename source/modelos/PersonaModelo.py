from basedatos.conecctiondb import conexion
from .entidades.persona import Persona

class PersonaModelo():

    @classmethod
    def get_personas(self):
        try:
            conexionn=conexion()
            personas=[]

            with conexionn.cursor() as cursor:
                cursor.execute("SELECT ci, nombre, primer_apellido, segundo_apellido, fecha_nacimiento FROM persona ")
                resulset=cursor.fetchall()

                for row in resulset:
                    persona=Persona(row[0],row[1],row[2],row[3],row[4])
                    personas.append(persona.to_JSON())

            conexionn.close()
            return personas
        except Exception as ex:
            raise Exception (ex)
        

    @classmethod
    def get_persona(self, ci):
        try:
            conexionn=conexion()

            with conexionn.cursor() as cursor:
                cursor.execute("SELECT ci, nombre, primer_apellido, segundo_apellido, fecha_nacimiento FROM persona WHERE ci= %s", (ci,))
                # aqui ya solo se utiliza row y fetchone ya que solo se mostrara un registro
                row=cursor.fetchone()

                persona=None
                if row != None:
                    persona=Persona(row[0],row[1],row[2],row[3],row[4])
                    persona=persona.to_JSON()

            conexionn.close()
            return persona
        except Exception as ex:
            raise Exception (ex)
        
    @classmethod
    def anadir_persona(self, persona):
        try:
            conexionn=conexion()

            with conexionn.cursor() as cursor:
                cursor.execute("""INSERT INTO persona (ci, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s)""",(persona.ci, persona.nombre, persona.primer_apellido, persona.segundo_apellido, persona.fecha_nacimiento))
                filas_afectadas=cursor.rowcount
                conexionn.commit()

            conexionn.close()
            return filas_afectadas
        except Exception as ex:
            raise Exception (ex)
        
    @classmethod
    def eliminar_persona(self, persona):
        try:
            conexionn=conexion()

            with conexionn.cursor() as cursor:
                cursor.execute("DELETE FROM persona WHERE ci =%s", (persona.ci,))
                filas_afectadas=cursor.rowcount
                conexionn.commit()

            conexionn.close()
            return filas_afectadas
        except Exception as ex:
            raise Exception (ex)
        
    @classmethod
    def modificar_persona(self, persona):
        try:
            conexionn=conexion()

            with conexionn.cursor() as cursor:
                cursor.execute("""UPDATE persona SET nombre=%s, primer_apellido=%s, segundo_apellido=%s, fecha_nacimiento=%s WHERE ci =%s""",(persona.nombre, persona.primer_apellido, persona.segundo_apellido, persona.fecha_nacimiento, persona.ci))
                filas_afectadas=cursor.rowcount
                conexionn.commit()

            conexionn.close()
            return filas_afectadas
        except Exception as ex:
            raise Exception (ex)
        

    @classmethod
    def get_promedio(self, ci):
        try:
            conexionn=conexion()

            with conexionn.cursor() as cursor:
                cursor.execute("SELECT AVG(EXTRACT(YEAR FROM AGE(NOW(),fecha_nacimiento))) AS promedio_edad FROM persona WHERE ci= %s", (ci,))
                # aqui ya solo se utiliza row y fetchone ya que solo se mostrara un registro
                row=cursor.fetchone()

                persona=None
                if row != None:
                    persona=row

            conexionn.close()
            return persona
        except Exception as ex:
            raise Exception (ex)

