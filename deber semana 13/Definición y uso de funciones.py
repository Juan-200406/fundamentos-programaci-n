# Definición de una función simple que saluda al usuario
def saludar(nombre):
    """
    Esta función toma un nombre como argumento
    y muestra un saludo personalizado.
    """
    mensaje = f"Hola, {nombre}! aqui esta el deber de pogramacion"
    return mensaje

# Llamada a la función
nombre_usuario = "ing walter"
saludo = saludar(nombre_usuario)

# Mostrar el resultado
print(saludo)
def temperaturas_promedio(calcular_temperaturas):
    temperaturas_promedio = {}
    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = (promedio)
    return temperaturas_promedio
# Creamos un diccionario de ciudades y temperaturas
ciudades_temperaturas = {
    "Nueva York": [22, 25, 26, 24, 23],
    "Los Ángeles": [28, 30, 29, 31, 27],
    "Chicago": [21, 20, 22, 18, 19],
    "Miami": [32, 33, 34, 30, 32],
    "Dallas": [26, 28, 27, 29, 25]
}
temperaturas_promedio = temperaturas_promedio(ciudades_temperaturas)
# Mostramos los resultados

print("temperaturas promedio por ciudad: ")
for ciudad,promedio in ciudades_temperaturas.items():
    print("{ciudad}: {promedio:.2f}°C")

