#Escritura de Archivo de Texto:
def saludar(nombre):
    mensaje = (f"hola {nombre} aqui esta el deber")
    return mensaje
ing = "ING Walter"
saludo = saludar(ing)
print(saludo)
#crear archivo
name = "my_notes.txt"
name  = open("my_notes.txt." ,"w")
#escribir en el archivo , metodo 1
name.write("linea 1: moises caicedo.\n")
name.write("linea 2: chelsea.\n")
# escribir en el archivo metodo 2
linea = ["linea 3: premier league.\n"]
name.writelines(linea)
# cerrar el archivo
name.close()
# abrir el archivo para leer de linea en linea
name= open("my_notes.txt." ,"r")
name = name.readlines()
# mostrar en la consola el contenido de cada linea
print(name)
