class Medicamento:
    def __init__(self, id, nombre, precio, descripcion, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad

    def dump(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'descripcion': self.descripcion,
            'cantidad': self.cantidad
        }