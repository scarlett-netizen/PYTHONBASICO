# Lista de días de la semana
my_list_2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

# Variable contador para repetir solo 3 veces
contador = 0

# Bucle while para repetir  el proceso 3 veces
while contador < 3:
    
    # Bucle for para recorrer la lista
    for dia in my_list_2:
        
        # Condición para no imprimir Lunes
        if dia != "Lunes":
            print(dia)
    
    contador += 1
