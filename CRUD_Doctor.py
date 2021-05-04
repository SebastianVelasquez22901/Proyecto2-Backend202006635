from flask.json import dump
from doctor import Doctor

class CRUD_Doctor:
    def __init__(self):
        self.doctores = []

    # Funcion para insertar un nuevo usuario
    def insertar(self, nombre, apellido, fecha_nacimiento, sexo, nombre_usuario, pwd, especialidad, telefono):
        id = len(self.doctores)
        self.doctores.append(Doctor(id, nombre, apellido, fecha_nacimiento, sexo, nombre_usuario, pwd, especialidad, telefono))
        return id

    # Funcion para obtener un usuario por id
    def obtener_porid(self, id):
        for doctor in self.doctores:
            if doctor.id == id:
                self.doctores.remove(doctor)           
                return doctor.dump()

        # No se encontro el usuario
        return None
    
    def login(self, nombre_usuario, pwd):
        for doctor in self.doctores:
            if doctor.nombre_usuario == nombre_usuario and doctor.pwd == pwd:
                return doctor.dump()
        return None
    
    
    
   


    def cargaMasiva(self, doctores_cm):
        for doctor in doctores_cm:
            self.insertar(doctor['nombre'], doctor['apellido'], doctor['fecha_nacimiento'], doctor['sexo'], doctor['nombre_usuario'], doctor['pdw'], doctor['especialidad'], doctor['telefono'])
        return "OK"

    def obtener_todos(self):
        return [doctor.dump() for doctor in self.doctores]