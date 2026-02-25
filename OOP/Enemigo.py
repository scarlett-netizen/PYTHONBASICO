class Enemigo:
    tipo_Enemigo: str
    puntos_energia: int = 10
    ataque = 1

    def __init__(self, tipo_Enemigo, puntos_energia=10, ataque=1):
        self._tipo_Enemigo = tipo_Enemigo
        self.puntos_energia = puntos_energia
        self.ataque = ataque

    def get_tipo_Enemigo(self):
        return self._tipo_Enemigo

    def habla(self):
        print(f"Yo soy {self._tipo_Enemigo}. preparado para pelear!!")

    def camina(self):
        print(f"{self._tipo_Enemigo} se mueve cerca de ti!!!")