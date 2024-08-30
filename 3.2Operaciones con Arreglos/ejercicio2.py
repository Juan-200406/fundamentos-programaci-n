#ejercicio 2 Matriz de 3 x 3
matriz = [
    [19, 84, 47],
    [56, 21, 76],
    [69, 78, 89]
]

print(matriz)
#Metodo de Ordenamiento buble_sort
def buble_sort(fila):
    #algoritmo buble sort
     n = len(fila)
     for i in range(n):
         for j in range(n-1, i, -1):
             if fila[j] > fila[j-1]:
                 fila[j], fila[j-1] = fila[j-1], fila[j]
                 print(fila)

print("matriz original")
print(matriz)
buble_sort(matriz[0])
print(matriz)