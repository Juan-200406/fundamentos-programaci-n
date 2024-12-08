# clases y objetos
"""class persona:
    jugador1 = "caicedo"
class persona1:
    jugador2 = "sarmiento"
print(persona1.jugador2)
"metodo 2"
class ligapro:
    pass
idv = ligapro()
ldu = ligapro()
#objetos.atributos = valor
idv.ligapro = "primera_etapa"
ldu.ganador = "segunda_etapa"
print(idv.ligapro)
print(ldu.ganador)
#metodos

#class Tienda:
 #   def __int__(self , b2, n2 ):
  #     self.carne = b2 * n2
   #    self.carne = n1 + n4
#calculo = Tienda ()
#print(calculo.carne)""

# funciones para atributos
class personas:
    nombre = "thiago"
    edad = 100
culturista = personas()
print(culturista.nombre)
print("la edad es ",getattr(culturista,"edad"))
#cambio de valor del atributo de un objecto
setattr(culturista,"edad",200)
print("ahora la edad es ",getattr(culturista,"edad"))
#eliminar atributo de un objeto
delattr(personas,"edad")"""""

# metodo construtor
class Topo:
    def __init__(self, nombre, ano):
        self.nombre = nombre
        self.ano = ano

    def discripcion(self):
        return "{} tiene: {} ".format(self.nombre, self.ano)

    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre, frase)

m = Topo("Carlos", 3000000000)
print(m.discripcion())

#herencia
class Pelota:
    def __init__(self, forma, tamaño):
        self.forma = forma
        self.tamaño = tamaño

    def dis(self):
        return "{} tiene forma de: {}".format(self.forma, self.tamaño)

class mancuerna(Pelota):
    def peso(self, kg):
        return "{} tiene un peso de: {} kg".format(self.forma, kg)

# Crear una instancia de Mancuerna
mancuerna = mancuerna("redonda", 41)
pelota = mancuerna("balon.","circulo")
print(mancuerna.dis())
print(mancuerna.peso(10))
