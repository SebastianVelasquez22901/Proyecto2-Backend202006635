class Paciente:
    def __init__(self, id, nombre, apellido, fecha_nacimiento, sexo, nombre_usuario, pwd, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.nombre_usuario = nombre_usuario
        self.pwd = pwd
        self.telefono = telefono

    def dump(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'fecha_nacimiento': self.fecha_nacimiento,
            'sexo': self.sexo,
            'nombre_usuario': self.nombre_usuario,
            'pwd': self.pwd,
            'telefono': self.telefono
        }