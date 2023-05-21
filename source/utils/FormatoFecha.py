import datetime

class FormatoFecha():
# ESTA PARTE DEL CODIGO ME AYUDA A TENER UN FORMATO DE FECHA MAS ENTENDIBLE FACIL MANEJO
    @classmethod
    def convertir_fecha(self, date):
        return datetime.datetime.strftime(date,'%d/%m/%Y')