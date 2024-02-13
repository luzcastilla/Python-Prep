#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:

# lista para números negativos
numeros_negativos = []

# Inicializar a -15
numero = -15

while numero < 0:
    numeros_negativos.append(numero)
    numero += 1

# Imprimir lista de negativos
print("Números negativos:", numeros_negativos)



# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:

numeros_negativos = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

indice = 0

while indice < len(numeros_negativos):
    if numeros_negativos[indice] % 2 == 0:
        print(numeros_negativos[indice])
    indice += 1

# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

numeros_negativos = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

for indice, numero in enumerate(numeros_negativos):
    if numero % 2 == 0:
        print(numero)

# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:

numeros_negativos = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

for indice, numero in enumerate(numeros_negativos):
    if indice < 3:
        print(numero)


# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:

numeros_negativos = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

for indice, numero in enumerate(numeros_negativos):
    print("Índice:", indice, "Valor:", numero)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:

lista = [1, 2, 5, 7, 8, 10, 13, 14, 15, 17, 20]

# almacenar los valores faltantes
valores_faltantes = []

for numero in range(1, 21):
    if numero not in lista:
        valores_faltantes.append(numero)

print("Valores faltantes:", valores_faltantes)

# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

fibonacci = [0, 1]

for i in range(2, 30):
    # sumar los dos números anteriores
    siguiente_numero = fibonacci[i - 1] + fibonacci[i - 2]
    # agregar el siguiente número a la lista
    fibonacci.append(siguiente_numero)

print("Los primeros treinta números de la sucesión de Fibonacci son:", fibonacci)


# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]

# Calcular la suma de todos los elementos de la lista
suma_fibonacci = sum(fibonacci)

print("La suma de todos los elementos de la lista es:", suma_fibonacci)


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>

# In[38]:

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]

ultimos_5_numeros = fibonacci[-5:]

for i in range(4, 0, -1):
    cociente = ultimos_5_numeros[i - 1] / ultimos_5_numeros[i]
    print(f"Cociente entre {ultimos_5_numeros[i - 1]} y {ultimos_5_numeros[i]}:", cociente)


# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for i in range(len(cadena)):
    if cadena[i] == 'n':
        print(f'La letra "n" aparece en la posición {i}')


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:

mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

iterador_claves = iter(mi_diccionario)

for clave in iterador_claves:
    print(clave)


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:


cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

lista_cadena = list(cadena)

iterador_lista = iter(lista_cadena)

for caracter in iterador_lista:
    print(caracter)



# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b', 'c', 'd']

tupla = tuple(zip(lista1, lista2))

print(tupla)



# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

lis = [18, 21, 29, 32, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100]
# lista con los números divisibles por 7
nueva_lista = [num for num in lis if num % 7 == 0]

print(nueva_lista)

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

lis = [[1, 2, 3, 4], 'rojo', 'verde', [True, False, False], ['uno', 'dos', 'tres']]

cantidad_total = sum(len(sublista) if isinstance(sublista, list) else 1 for sublista in lis)

print("La cantidad total de elementos en la lista es:", cantidad_total)

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

lis = [[1, 2, 3, 4], 'rojo', 'verde', [True, False, False], ['uno', 'dos', 'tres']]

nueva_lista = [elemento if isinstance(elemento, list) else [elemento] for elemento in lis]

print(nueva_lista)
