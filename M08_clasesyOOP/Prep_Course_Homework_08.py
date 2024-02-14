#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:

class Vehículo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada

vehículo1 = Vehículo("rojo", "auto", 2000)
print("Color:", vehículo1.color)
print("Tipo:", vehículo1.tipo)
print("Cilindrada:", vehículo1.cilindrada)


# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:
class Vehículo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada

    def acelerar(self):
        print("Acelerando...")

    def frenar(self):
        print("Frenando...")

    def doblar(self, direccion):
        print("Doblando hacia", direccion)

vehículo1 = Vehículo("rojo", "auto", 2000)
vehículo1.acelerar()
vehículo1.frenar()
vehículo1.doblar("izquierda")




# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:


Copy code
class Vehículo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada

    def acelerar(self):
        print("Acelerando...")

    def frenar(self):
        print("Frenando...")

    def doblar(self, direccion):
        print("Doblando hacia", direccion)

vehículo1 = Vehículo("rojo", "auto", 2000)
vehículo2 = Vehículo("azul", "camioneta", 2500)
vehículo3 = Vehículo("verde", "moto", 600)

# Ejecutar métodos en cada objeto
print("Vehículo 1:")
vehículo1.acelerar()
vehículo1.frenar()
vehículo1.doblar("derecha")

print("\nVehículo 2:")
vehículo2.acelerar()
vehículo2.frenar()
vehículo2.doblar("izquierda")

print("\nVehículo 3:")
vehículo3.acelerar()
vehículo3.frenar()
vehículo3.doblar("izquierda")



# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:
class Vehículo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = "recto"

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        if self.velocidad >= 10:
            self.velocidad -= 10
        else:
            self.velocidad = 0

    def doblar(self, direccion):
        self.direccion = direccion

    def mostrar_estado(self):
        print("Velocidad:", self.velocidad)
        print("Dirección:", self.direccion)

    def mostrar_informacion(self):
        print("Color:", self.color)
        print("Tipo:", self.tipo)
        print("Cilindrada:", self.cilindrada)

vehículo1 = Vehículo("rojo", "auto", 2000)
vehículo1.mostrar_informacion()
print()
vehículo1.acelerar()
vehículo1.mostrar_estado()
print()
vehículo1.doblar("izquierda")
vehículo1.mostrar_estado()





# In[13]:






# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:


class Utilidades:
    @staticmethod
    def verificar_primo(numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    @staticmethod
    def valor_modal(lista):
        contador = {}
        for elemento in lista:
            if elemento in contador:
                contador[elemento] += 1
            else:
                contador[elemento] = 1
        moda = max(contador.values())
        modas = [elemento for elemento, frecuencia in contador.items() if frecuencia == moda]
        return modas

    @staticmethod
    def convertir_grados(grados, unidad_origen, unidad_destino):
        if unidad_origen.lower() == 'celsius':
            if unidad_destino.lower() == 'fahrenheit':
                return (grados * 9/5) + 32
            elif unidad_destino.lower() == 'kelvin':
                return grados + 273.15
        elif unidad_origen.lower() == 'fahrenheit':
            if unidad_destino.lower() == 'celsius':
                return (grados - 32) * 5/9
            elif unidad_destino.lower() == 'kelvin':
                return (grados - 32) * 5/9 + 273.15
        elif unidad_origen.lower() == 'kelvin':
            if unidad_destino.lower() == 'celsius':
                return grados - 273.15
            elif unidad_destino.lower() == 'fahrenheit':
                return (grados - 273.15) * 9/5 + 32
        return None

    @staticmethod
    def factorial(numero):
        if numero < 0:
            return None
        elif numero == 0:
            return 1
        else:
            resultado = 1
            for i in range(1, numero + 1):
                resultado *= i
            return resultado

print(Utilidades.verificar_primo(17))
print(Utilidades.valor_modal([1, 2, 3, 4, 4, 5, 5, 5]))
print(Utilidades.convertir_grados(100, 'celsius', 'fahrenheit'))
print(Utilidades.factorial(5))



# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:





# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:

# Crear una instancia de la clase Utilidades (no necesario, pero posible)
utilidades = Utilidades()

# Probar la función verificar_primo
print("¿Es 17 un número primo?", Utilidades.verificar_primo(17))

# Probar la función valor_modal
print("El valor modal de la lista [1, 2, 3, 4, 4, 5, 5, 5] es:", Utilidades.valor_modal([1, 2, 3, 4, 4, 5, 5, 5]))

# Probar la función convertir_grados
print("100 grados Celsius equivalen a", Utilidades.convertir_grados(100, 'celsius', 'fahrenheit'), "grados Fahrenheit")

# Probar la función factorial
print("El factorial de 5 es:", Utilidades.factorial(5))


# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:
# En el archivo utilidades.py

class Utilidades:
    @staticmethod
    def verificar_primo(numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    @staticmethod
    def valor_modal(lista):
        contador = {}
        for elemento in lista:
            if elemento in contador:
                contador[elemento] += 1
            else:
                contador[elemento] = 1
        moda = max(contador.values())
        modas = [elemento for elemento, frecuencia in contador.items() if frecuencia == moda]
        return modas

    @staticmethod
    def convertir_grados(grados, unidad_origen, unidad_destino):
        if unidad_origen.lower() == 'celsius':
            if unidad_destino.lower() == 'fahrenheit':
                return (grados * 9/5) + 32
            elif unidad_destino.lower() == 'kelvin':
                return grados + 273.15
        elif unidad_origen.lower() == 'fahrenheit':
            if unidad_destino.lower() == 'celsius':
                return (grados - 32) * 5/9
            elif unidad_destino.lower() == 'kelvin':
                return (grados - 32) * 5/9 + 273.15
        elif unidad_origen.lower() == 'kelvin':
            if unidad_destino.lower() == 'celsius':
                return grados - 273.15
            elif unidad_destino.lower() == 'fahrenheit':
                return (grados - 273.15) * 9/5 + 32
        return None

    @staticmethod
    def factorial(numero):
        if numero < 0:
            return None
        elif numero == 0:
            return 1
        else:
            resultado = 1
            for i in range(1, numero + 1):
                resultado *= i
            return resultado
Ahora, desde otro archivo, podemos importar la clase Utilidades y probar alguna de sus funciones:

python
Copy code
# En otro archivo .py

from utilidades import Utilidades

# Probar la función verificar_primo
print("¿Es 17 un número primo?", Utilidades.verificar_primo(17))

# Probar la función valor_modal
print("El valor modal de la lista [1, 2, 3, 4, 4, 5, 5, 5] es:", Utilidades.valor_modal([1, 2, 3, 4, 4, 5, 5, 5]))

# Probar la función convertir_grados
print("100 grados Celsius equivalen a", Utilidades.convertir_grados(100, 'celsius', 'fahrenheit'), "grados Fahrenheit")

# Probar la función factorial
print("El factorial de 5 es:", Utilidades.factorial(5))



