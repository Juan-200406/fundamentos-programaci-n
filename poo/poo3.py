#polimorfismo
class animales:
    def __init__(self,animale ):
        self.animal= animale
    def tipo_animal(self):
        pass
class leon (animales):
    def tipo_animal(self):
        print("animal salvaje")
class perro (animales):
    def tipo_animal(self):
        print("animal domestico")
nuevo_animal = leon("dogi")
print(nuevo_animal.tipo_animal())

#polimorfismo por funcion
class tomate:
    def tipo(self):
        print("vegetal")
    def color(self):
        print("rojo")
class manzana:
    def tipo(self):
        print("fruta")
    def color(self):
        print("verde")
def funcion(objeto):
    objeto.tipo()
    objeto.color()
nuevo_tomate = tomate()
print(funcion(nuevo_tomate))
nueva_manzana = manzana()
print(funcion(nueva_manzana))
#polimorfismo por metodo
class colombia:
    def capital(self):
        print("bogota")
    def idioma(self):
        print("español")
class francia:
    def capital(self):
        print("quito")
    def idioma(self):
        print("frances")
colombiano = colombia()
frances = francia()
for i in (colombiano,frances):
    i.capital()
    i.idioma()
#polimorfismo por  herencia
class ave:
    def volar(self):
        print("las aves pueden volar")
class gallina(ave):
    def volar(self):
        print("las gallinas no pueden volar")
class aguila:
    def volar(self):
        print("las aguilas pueden volar")
obj_avesjk = ave()
obj_gallinasss = gallina()
obj_aguilass = aguila()
print(obj_avesjk.volar())
print(obj_gallinasss.volar())
print(obj_aguilass.volar())
# metodo super
class mamifero:
    def __init__(self,nombre):
        print(nombre,"es  un animal de sangre caliente")
class leon(mamifero):
    def _init_(self):
        print("el leon tiene 4 patas")
        super().__init__("foco")
n_leon= leon()
print(n_leon.leon())