from flask.json import dump
from enfermero import Enfermero

class CRUD_Enfermero:
    def __init__(self):
        self.enfermeros = []

    def insertar(self, nombre, apellido, fecha_nacimiento, sexo, nombre_usuario, pwd, telefono):
        id = len(self.enfermeros)
        self.enfermeros.append(Enfermero(id, nombre, apellido, fecha_nacimiento, sexo, nombre_usuario, pwd, telefono))
        return id

    def obtener_porid(self, id):
        for enfermero in self.enfermeros:
            if enfermero.id == id:
                self.enfermeros.remove(enfermero)           
                return enfermero.dump()

        # No se encontro el usuario
        return None

    def login(self, nombre_usuario, pwd):
        for enfermero in self.enfermeros:
            if enfermero.nombre_usuario == nombre_usuario and enfermero.pwd == pwd:
                return enfermero.dump()

        return None

    def cargaMasiva(self, enfermeros_cm):
        for enfermero in enfermeros_cm:
            self.insertar(enfermero['nombre'], enfermero['apellido'], enfermero['fecha_nacimiento'], enfermero['sexo'], enfermero['nombre_usuario'], enfermero['pdw'], enfermero['telefono'])
        return "OK"

    def obtener_todos(self):
        return [enfermero.dump() for enfermero in self.enfermeros]