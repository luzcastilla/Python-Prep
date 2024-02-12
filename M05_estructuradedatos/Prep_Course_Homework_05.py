#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

ciudades = ["Tokio", "Nueva York", "Londres", "París", "Shanghái", "Moscú", "Seúl", "Ciudad de México", "Pekín", "El Cairo"]

print("Lista de ciudades del mundo:")
print(ciudades)


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print("El segundo elemento de la lista es:", ciudades[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:


print("Del segundo al cuarto elemento de la lista son:", ciudades[1:4])

# 4) Visualizar el tipo de dato de la lista

# In[12]:

print("El tipo de dato de la lista es:", type(ciudades))


# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:


print("Todos los elementos de la lista a partir del tercero:", ciudades[2:])


# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:


print("Los primeros 4 elementos de la lista son:", ciudades[:4])
 

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

ciudades_nuevas = ["Sidney"]
ciudades += ciudades_nuevas

print("Lista de ciudades después de agregar las nuevas:")
print(ciudades)

# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:


ciudades.insert(3, "Madrid")

print("Lista de ciudades después de agregar otra ciudad en la cuarta posición:")
print(ciudades)


# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:

otras_ciudades = ["Berlín", "Estambul"]
ciudades.extend(otras_ciudades)

print("Lista de ciudades después de concatenar otra lista:")
print(ciudades)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

indice_roma = ciudades.index("Roma")

print("El índice de la ciudad 'Roma' en la lista es:", indice_roma)

# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

try:
    indice_madrid = ciudades.index("Madrid")
    print("El índice de la ciudad 'Madrid' en la lista es:", indice_madrid)
except ValueError:
    print("La ciudad 'Madrid' no está en la lista.")



# 12) Eliminar un elemento de la lista

# In[25]:

ciudades.remove("Madrid")

print("Lista de ciudades después de eliminar 'Madrid':")
print(ciudades)



# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:


#Python lanzará una excepción ValueError


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:


ultimo_elemento = ciudades.pop()

print("Último elemento de la lista extraído:", ultimo_elemento)

print("Lista de ciudades después de extraer el último elemento:")
print(ciudades)


# 15) Mostrar la lista multiplicada por 4

# In[29]:

lista_multiplicada = ciudades * 4

print("Lista multiplicada por 4:")
print(lista_multiplicada)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

numeros_enteros = tuple(range(1, 21))

print("Tupla con los números enteros del 1 al 20:")
print(numeros_enteros)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print("Elementos de la tupla desde el índice 10 al 15:")
print(numeros_enteros[10:16])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:


numero_20_esta = 20 in numeros_enteros
numero_30_esta = 30 in numeros_enteros

print("¿20 está dentro de la tupla?", numero_20_esta)
print("30 está dentro de la tupla?", numero_30_esta)


# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:


if 'París' not in ciudades:
    # no está en la lista, agregarlo
    ciudades.append('París')
    mensaje = "Se agregó 'París' a la lista."
else:
    mensaje = "'París' ya existe en la lista."

print(mensaje)


# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:
elemento = 5

# en la tupla
cantidad_en_tupla = numeros_enteros.count(elemento)

print(f"El elemento {elemento} se encuentra {cantidad_en_tupla} veces en la tupla.")

#en la lista
cantidad_en_lista = ciudades.count("París")

print(f"El elemento 'París' se encuentra {cantidad_en_lista} veces en la lista.")


# 21) Convertir la tupla en una lista

# In[52]:

lista_numeros_enteros = list(numeros_enteros)

print("Lista de números enteros obtenida a partir de la tupla:")
print(lista_numeros_enteros)



# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:


primer_elemento, segundo_elemento, tercer_elemento, *_ = numeros_enteros

print("Primer elemento:", primer_elemento)
print("Segundo elemento:", segundo_elemento)
print("Tercer elemento:", tercer_elemento)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:

datos_ciudades = {"ciudad": ciudades}

datos_ciudades["Pais"] = "Francia"
datos_ciudades["Continente"] = "Europa"

print("Diccionario de datos de la ciudad:")
print(datos_ciudades)


# 24) Imprimir las claves del diccionario

# In[59]:

print("Claves del diccionario:")
print(datos_ciudades.keys())


# 25) Imprimir las ciudades a través de su clave

# In[61]:

print("Ciudades:")
print(datos_ciudades["ciudad"])


