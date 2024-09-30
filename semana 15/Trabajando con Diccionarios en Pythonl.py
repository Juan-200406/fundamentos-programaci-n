 #Crea un diccionario llamado informacion_personal que contenga información ficticia
# sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
#Acceder y Modificar Valores:

#Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
#Verificar Existencia de Claves:

#Verifica si la clave "telefono" existe en el diccionario. Si no existe,
# agrégala con un número de teléfono ficticio.
#Eliminar una Clave:

#Elimina la clave "edad" del diccionario, ya que esa información no es necesari
print("aqui esta mi trabajo : ")
informacion_personal = { "nombre" : "pablo" , "edad" : 22 , "ciudad" : "Madrid", "profesion" : "abogado"
}
print(informacion_personal["nombre"])
print(informacion_personal["edad"])
print(informacion_personal["ciudad"])
print(informacion_personal["profesion"])
#modificar ELEMENTO
informacion_personal["ciudad"] = "londres"
print(informacion_personal)
#agregar ELEMENTO
informacion_personal["profesion"] = "medico"
print(informacion_personal)
informacion_personal["telefono"]="099999999"
#eliminar ELEMENTO
del informacion_personal["edad"]
print(informacion_personal )