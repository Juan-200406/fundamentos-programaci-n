#herencia ejempo

"""class calculadora:
    def __init__(self, n1):
        self.n = n1
        self.datos = [0for i in range(self.n1)]
    def ingressardato(self):
        self.datos = [int(input("ingresar dato"+str(i+1))) for i in range(self.datos)]
class op_basicas(calculadora):
    def __init__(self,):
        calculadora.__init__(self, 4)

    def multiplicacion(self):
        a,b = self.datos
        m = a * b
        print("la multiplicacion es: ",m)
    def division(self):
        a,b = self.datos
        d = a / b
        print("la division es: ",d)

class raiz(calculadora):
        def __init__(self):
            calculadora.__init__(self,4)
    def cuadrada(self):
        import math
        a,= self.datos
        print("la cuadrada es: ",math.sqrt(a))
ejemplo = op_basicas()
print(ejemplo.ingressardato())
print(ejemplo.multiplicacion())
#comprbar si es true o false
print(isinstance(ejemplo,op_basicas))"""""

#herencia multiple
"""class telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("llamando")
    def ocupado(self):
        print("ocupado")
class reproducir:
    def __init__(self):
        pass
    def reproducir_musica(self):
        print("reproduciendo musica")
    def reproducir_video(self):
        print("reproduciendo video")
class smartpone(telefono,reproducir):
    def __del__(self):
        print("celular apagado")
movil = smartpone
print(movil.reproducir_musica())"""""
#para saber que metodos especiales tenemos que utilizar
#print(dir(movil))

# f-string

class estudiante:
    def __init__(self,nombre,edad,sexo = "m"):
        self.nombre= nombre
        self.edad = edad
        self.sexo = sexo
    def __repr__(self):
        return f"{self.nombre} {self.edad} {self.sexo}"
nuevo = estudiante("thiago",25,)
print(f"{nuevo}")

#metodo clase

class pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f"({self.ingredientes!r})"

    @classmethod
    def pastel_chocolate(cls):
        return cls(["harina", "leche", "chocolate"])

    @classmethod
    def pastel_vainilla(cls):
        return cls(["harina", "leche", "vainilla"])


# Imprime un pastel de vainilla
print(pastel.pastel_vainilla())

# Clase pastelito con método estático
import math


class pastelito:
    def __init__(self, ingredientes, tamanho):
        self.ingredientes = ingredientes
        self.tamanho = tamanho

    def __repr__(self):
        return f"pastelito({self.ingredientes}, {self.tamanho})"

    def area(self):
        return self.calcular_area(self.tamanho)

    @staticmethod
    def calcular_area(a):
        return (a ** 2) * math.pi


# Crear una instancia de pastelito y mostrar los ingredientes
nuevo_pastelito = pastelito(["harina", "leche"], 30)
print(nuevo_pastelito.ingredientes)
print(nuevo_pastelito.area())
