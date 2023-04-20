import json

class Producto:
    def __init__(self, id, precio, precio_unidad, unidad):
        self.id = id
        self.precio = precio
        self.precio_unidad = precio_unidad
        self.unidad = unidad

    def to_dict(self):
        return {
            "id": self.id,
            "precio": self.precio,
            "precio_unidad": self.precio_unidad,
            "unidad": self.unidad
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()
