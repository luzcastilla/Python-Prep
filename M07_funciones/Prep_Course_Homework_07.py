#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:


def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Ejemplo
print(es_primo(7))  # True
print(es_primo(12)) # False


# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

def numeros_primos(lista):
    primos = []
    for numero in lista:
        if es_primo(numero):
            primos.append(numero)
    return primos

# Ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = numeros_primos(numeros)
print(primos)  # Salida: [2, 3, 5, 7]


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

def numero_mas_repetido(lista):
    conteo = {}
    for numero in lista:
        if numero in conteo:
            conteo[numero] += 1
        else:
            conteo[numero] = 1
    
    mas_repetido = None
    repeticiones = 0
    for numero, frecuencia in conteo.items():
        if frecuencia > repeticiones:
            mas_repetido = numero
            repeticiones = frecuencia
    
    return mas_repetido, repeticiones

# Ejemplo
numeros = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6]
resultado = numero_mas_repetido(numeros)
print("Número más repetido:", resultado[0])
print("Veces que se repite:", resultado[1])



# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

# In[56]:

def convertir_temperatura(valor, medida_origen, medida_destino):
    if medida_origen == 'Celsius' and medida_destino == 'Fahrenheit':
        return (valor * 9/5) + 32
    elif medida_origen == 'Celsius' and medida_destino == 'Kelvin':
        return valor + 273.15
    elif medida_origen == 'Fahrenheit' and medida_destino == 'Celsius':
        return (valor - 32) * 5/9
    elif medida_origen == 'Fahrenheit' and medida_destino == 'Kelvin':
        return (valor - 32) * 5/9 + 273.15
    elif medida_origen == 'Kelvin' and medida_destino == 'Celsius':
        return valor - 273.15
    elif medida_origen == 'Kelvin' and medida_destino == 'Fahrenheit':
        return (valor - 273.15) * 9/5 + 32
    else:
        return "Medidas de temperatura no válidas"

# Ejemplo
resultado = convertir_temperatura(25, 'Celsius', 'Fahrenheit')
print("25 grados Celsius son", resultado, "grados Fahrenheit")

# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:

def convertir_temperatura(valor, medida_origen, medida_destino):
    if medida_origen == 'Celsius' and medida_destino == 'Fahrenheit':
        return (valor * 9/5) + 32
    elif medida_origen == 'Celsius' and medida_destino == 'Kelvin':
        return valor + 273.15
    elif medida_origen == 'Fahrenheit' and medida_destino == 'Celsius':
        return (valor - 32) * 5/9
    elif medida_origen == 'Fahrenheit' and medida_destino == 'Kelvin':
        return (valor - 32) * 5/9 + 273.15
    elif medida_origen == 'Kelvin' and medida_destino == 'Celsius':
        return valor - 273.15
    elif medida_origen == 'Kelvin' and medida_destino == 'Fahrenheit':
        return (valor - 273.15) * 9/5 + 32
    else:
        return "Medidas de temperatura no válidas"

# Valores de temperatura
temperaturas = [25, 32, 100]

# Iterar sobre las combinaciones 
for medida_origen in ['Celsius', 'Fahrenheit', 'Kelvin']:
    for medida_destino in ['Celsius', 'Fahrenheit', 'Kelvin']:
        if medida_origen != medida_destino:  # Evitar conversión de una misma medida a sí misma
            for valor in temperaturas:
                resultado = convertir_temperatura(valor, medida_origen, medida_destino)
                print(f"{valor} grados {medida_origen} son {resultado:.2f} grados {medida_destino}")


# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:


def factorial(numero):
    try:
        # Verificar si el número es negativo
        if numero < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        
        # Verificar si el número no es entero
        if not isinstance(numero, int):
            raise ValueError("El factorial solo está definido para números enteros.")
        
        # Calcular el factorial
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        
        return resultado
    
    except ValueError as error:
        return str(error)

# Ejemplo
print(factorial(5))    
print(factorial(0))   
print(factorial(-5))  
print(factorial(3.5))  

