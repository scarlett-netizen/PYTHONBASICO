print("======== MI SUPER CALCULADORA ==========")

# Pedimos los datos al usuarios
num_1 = float(input("Escribe el valor del primer número: "))
num_2 = float(input("Escribe el valor del segundo número: "))
operacion = input("¿Qué operación deseas hacer? (+, -, *, /): ")

# Función principal de la calculadora
def calculadora(num_1, num_2, operacion):
    
    if operacion == "+":
        return num_1 + num_2
    
    elif operacion == "-":
        return num_1 - num_2
    
    elif operacion == "*":
        return num_1 * num_2
    
    elif operacion == "/":
        # que no se divida entre cero
        if num_2 == 0:
            return "Error: No se puede dividir entre cero."
        return num_1 / num_2
    
    else:
        return "Operación no válida."

# el resultado  se guarda llamandolo función
resultado = calculadora(num_1, num_2, operacion)

print("Resultado:", resultado)
