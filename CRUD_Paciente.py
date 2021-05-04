from flask.json import dump
from paciente import Paciente

class CRUD_Paciente:
    def __init__(self):
        self.pacientes = []

    def insertar(self, nombre, apellido, fecha_nacimiento, sexo, nombre_usuario, pwd, telefono):
        id = len(self.pacientes)
        self.pacientes.append(Paciente(id, nombre, apellido, fecha_nacimiento, sexo, nombre_usuario, pwd, telefono))
        return id

    def obtener_porid(self, id):
        for paciente in self.pacientes:
            if paciente.id == id:
                self.pacientes.remove(paciente)           
                return paciente.dump()

        # No se encontro el usuario
        return None

    def login(self, nombre_usuario, pwd):
        for paciente in self.pacientes:
            if paciente.nombre_usuario == nombre_usuario and paciente.pwd == pwd:
                return paciente.dump()

        return None

    def cargaMasiva(self, pacientes_cm):
        for paciente in pacientes_cm:
            self.insertar(paciente['nombre'], paciente['apellido'], paciente['fecha_nacimiento'], paciente['sexo'], paciente['nombre_usuario'], paciente['pdw'], paciente['telefono'])
        return "OK"

    def obtener_todos(self):
        return [paciente.dump() for paciente in self.pacientes]