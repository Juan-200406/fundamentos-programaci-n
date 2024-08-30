#  Matriz de 3 x 3
matriz = [
    [82, 14, 67],
    [20, 80, 90],
    [56, 78, 99]
]

print(matriz)
# Funcion buscado_valor especifico
def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i,j


valor_buscado = 78
#print(buscar_valor(matriz,valor_buscado))

if valor_buscado == valor_buscado:
   print("Valor encontrado",buscar_valor(matriz,valor_buscado))
else:
    print("Valor incorrecto")