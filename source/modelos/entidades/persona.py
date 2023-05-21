from utils.FormatoFecha import FormatoFecha


class Persona():

    def __init__(self, ci=None, nombre=None, primer_apellido=None, segundo_apellido=None, fecha_nacimiento=None) -> None:
        self.ci=ci
        self.nombre=nombre
        self.primer_apellido=primer_apellido
        self.segundo_apellido=segundo_apellido
        self.fecha_nacimiento=fecha_nacimiento

    def to_JSON(self):
        return {
            'ci': self.ci,
            'nombre': self.nombre,
            'primer_apellido':self.primer_apellido,
            'segundo_apellido':self.segundo_apellido,
            'fecha_nacimiento':FormatoFecha.convertir_fecha(self.fecha_nacimiento)
        }