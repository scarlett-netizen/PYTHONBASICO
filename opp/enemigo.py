# Definición de una clase básica
class Persona:
    # El método __init__ es el constructor (se ejecuta al crear el objeto)
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo

    # Un método (función dentro de la clase)
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto (instancia de la clase)
usuario = Persona("Scarlett", 20)

# Llamar al método
usuario.saludar()
