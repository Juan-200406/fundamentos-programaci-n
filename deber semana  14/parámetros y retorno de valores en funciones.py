# Crea una función llamada calcular_descuento que tome dos parámetros:
# el monto total de la compra y un valor predeterminado para el porcentaje de descuento
# (por ejemplo, 10% por defecto).
# La función debe calcular el
# descuento aplicando el porcentaje al monto total de la compra.
# La función debe devolver el monto del descuento calculado.
# Llamada a la Función:
# Llama a la función calcular_descuento al menos dos veces desde el programa principal.
# En una llamada, proporciona el monto total de la compra y, en la otra, proporciona tanto el monto total de la compra como el porcentaje de descuento.
# Salida de Resultados:
# Muestra los resultados de las llamadas a la función, incluyendo el monto del descuento y
# el monto final a pagar después del descuento#



def calcular_descuento (monto_total, descuento=50 ):

    resultado = monto_total * descuento / 100
    return resultado

res=calcular_descuento(100)
print(f"el decuento es de",res)

res2=calcular_descuento(100,2)
print(f"el decuento es de",res2)

