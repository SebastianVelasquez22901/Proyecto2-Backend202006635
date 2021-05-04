from flask.json import dump
from medicamento import Medicamento

class CRUD_Medicamento:
    def __init__(self):
        self.medicamentos = []

    def insertar(self, nombre, precio, descripcion, cantidad):
        id = len(self.medicamentos)
        self.medicamentos.append(Medicamento(id, nombre, precio, descripcion, cantidad))
        return id

    def obtener_porid(self, id):
        for medicamento in self.medicamentos:
            if medicamento.id == id:
                self.medicamentos.remove(medicamento)           
                return medicamento.dump()

        # No se encontro el usuario
        return None


    def cargaMasiva(self, medicamentos_cm):
        for medicamento in medicamentos_cm:
            self.insertar(medicamento['nombre'], medicamento['precio'], medicamento['descripcion'], medicamento['cantidad'])
        return "OK"

    def obtener_todos(self):
        return [medicamento.dump() for medicamento in self.medicamentos]