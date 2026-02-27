from enemigo import *

class zombie(Enemigo):
    def __init_ (self, puntos_energia=10, ataque =1 ):
        super()._init_(tipo_enemigo='zombie', puntos_energia = puntos_energia, ataque=ataque)
    def habla(self):
        print("hummmmm...*")
    def propagar_emfermedad(self):
        print("El zombie esta tratando de propagar 1s enfermedad!!")